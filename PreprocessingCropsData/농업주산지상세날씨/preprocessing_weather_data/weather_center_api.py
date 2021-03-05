import urllib
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd
import xml.etree.ElementTree as ET


# 작물별 데이터를 csv 로 저장 (2001-2019 까지 모든 날짜, 모든 지역)
def weatherData_to_csv_byStation(serviceKey, station_name, start_year, end_year):

    # url
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    attributes = ["stnId", "stnNm", "tm", "avgTa", "minTa", "minTaHrmt",
           "maxTa", "maxTaHrmt", "mi10MaxRnHrmt", "hr1MaxRn", "hr1MaxRnHrmt", "sumRn",
           "maxInsWs", "maxInsWsWd", "maxInsWsHrmt", "maxWs", "maxWsWd", "maxWsHrmt",
           "avgWs", "hr24SumRws", "maxWd", "avgTd", "minRhm", "minRhmHrmt",
           "avgRhm", "avgPv", "avgPa", "maxPs", "maxPsHrmt", "minPs",
           "minPsHrmt", "avgPs", "ssDur", "sumSsHr", "hr1MaxIcsrHrmt", "hr1MaxIcsr",
           "sumGsr", "ddMefs", "ddMefsHrmt", "ddMes", "ddMesHrmt", "sumDpthFhsc",
           "avgTca", "avgLmac", "avgTs", "minTg", "avgCm5Te", "avgCm10Te",
           "avgCm20Te", "avgCm30Te", "avgM05Te", "avgM10Te", "avgM15Te", "avgM30Te",
           "avgM50Te", "sumLrgEv", "sumSmlEv", "n99Rn", "iscs", "sumFogDur"]
    # attributes
    columns = [
        "지점 번호", "지점명", "시간", "평균 기온", "최저 기온", "최저 기온 시각", "최고 기온",
        "최대 기온 시각", "10분 최다강수량 시각", "1시간 최다강수량", "1시간 최다 강수량 시각", "일강수량", "최대 순간풍속",
        "최대 순간 풍속 풍향", "최대 순간풍속 시각", "최대 풍속", "최대 풍속 풍향", "최대 풍속 시각", "평균 풍속",
        "풍정합", "최대 풍향", "평균 이슬점온도", "최소 상대습도", "평균 상대습도 시각", "평균 상대습도",
        "평균 증기압", "평균 현지기압", "최고 해면 기압", "최고 해면기압 시각", "최저 해면기압", "최저 해면기압 시각",
        "평균 해면기압", "가조시간", "합계 일조 시간", "1시간 최다 일사량 시각", "1시간 최다 일사량", "합계 일사",
        "일 최심신적설", "일 최심신적설 시각", "일 최심적설", "일 최심적설 시각", "합계 3시간 신적설", "평균 전운량",
        "평균 중하층운량", "평균 지면온도", "최저 초상온도", "평균 5cm 지중온도", "평균10cm 지중온도", "평균 20cm 지중온도",
        "평균 30cm 지중온도", "0.5m 지중온도", "1.0m 지중온도", "1.5m 지중온도", "3.0m 지중온도", "5.0m 지중온도",
        "합계 대형증발량", "합계 소형증발량", "9-9강수", "일기현상", "안개 계속 시간"
    ]

    # 데이터 요청 시작 (진행 상황 표시)
    print("Start to get area_weather_data ...")

    # df_for_storage = pd.DataFrame(columns=columns)
    # df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")

    serviceKey = unquote(serviceKey)


    file_name = "../weather_data/일기상자료_" + station_name + "_" + str(start_year) + "_" + str(end_year) + ".csv"

    df_for_storage = pd.DataFrame(columns=columns)
    df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")

    # 모든 페이지를 조회하는 while, 데이터가 없는 page 일 경우 종료
    for year in range(start_year, end_year + 1):
        start_ymd = "%d0101" % year
        end_ymd = "%d1231" % year

        df = pd.DataFrame()
        queryParams = '?' + urlencode({quote_plus('ServiceKey'): serviceKey,
                                       quote_plus('pageNo'): "1",
                                       quote_plus('numOfRows'): '500',
                                       quote_plus('dataType'): 'XML',
                                       quote_plus('dataCd'): 'ASOS',
                                       quote_plus('dateCd'): 'DAY',
                                       quote_plus('startDt'): start_ymd,
                                       quote_plus('endDt'): end_ymd,
                                       quote_plus('stnIds'): s_code})

        rq = urllib.request
        body = rq.urlopen(url + queryParams)
        rq.get_method = lambda: 'GET'
        response_body = body.read()
        result = response_body.decode('utf-8')

        # XML 형식의 API Response 를 읽기 위한 ElementTree
        # XMl 형식이지만 type 은 string 이므로 fromstring 메소드 사용
        tree = ET.ElementTree(ET.fromstring(result))
        root = tree.getroot()  # 최상위 노드 root

        # resultMsg 태그를 읽어 NO_DATA 인지 확인
        resultMsg = root[0][1].text

        print(resultMsg)

        if resultMsg == "NO_DATA":
            print("No Data", station_name, year)
            continue

        elif resultMsg != "NORMAL_SERVICE":
            print("ERROR :", resultMsg)
            print("End")
            continue

        # root 는 header(응답 정보) 와 body(데이터)로 구성
        # root[1] 은 body, root[1][1] 은 items
        items = root[1][1]

        for item in items:
            row = dict()
            for value in item:
                row[value.tag] = value.text
                # print(value.tag, value.text)

            df = df.append(row, ignore_index=True)

        # 내가 정한 col 만 가져옴
        df = df[attributes]

        # col 명 한글로 바꿈
        df.columns = columns

        print(station_name, "year :", year)

        # excel 파일에 이어서 저장
        df.to_csv(file_name, mode="a", header=False, index=False, encoding="utf-8-sig")


# 날씨 데이터를 csv 로 저장 (2017-12-21 ~ 24 까지 모든 날짜, 모든 지역)
def OutlierStatistics_to_csv(serviceKey, file_name, start_ymd, end_ymd):
    # 관측 지점 코드
    station_code_csv = pd.read_csv("관측지점코드.csv", sep="\t")

    station_code = station_code_csv["지점"]

    # url
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'

    # attributes
    attributes = [
        "stnNm", "avgRhm", "avgTa", "avgWs",
        "maxTa", "minRhm", "minTa", "sumRn",
        "sumSsHr", "tm"
    ]

    columns = ['지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속',
               '일 최고기온', '일 최저상대습도', '일 최저기온', '일 강수량',
               '일 누적일조시간', '연월일']

    # 데이터 요청 시작 (진행 상황 표시)
    print("Start to get area_weather_data:")

    # df_for_storage = pd.DataFrame(columns=columns)
    # df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")

    serviceKey = unquote(serviceKey)

    df = pd.DataFrame()

    for s_code in station_code:

        queryParams = '?' + urlencode({quote_plus('ServiceKey'): serviceKey,
                                       quote_plus('pageNo'): '1',
                                       quote_plus('numOfRows'): '10',
                                       quote_plus('dataType'): 'XML',
                                       quote_plus('dataCd'): 'ASOS',
                                       quote_plus('dateCd'): 'DAY',
                                       quote_plus('startDt'): start_ymd,
                                       quote_plus('endDt'): end_ymd,
                                       quote_plus('stnIds'): s_code})

        request = Request(url + queryParams)
        request.get_method = lambda: 'GET'
        response_body = urlopen(request).read()
        result = response_body.decode('utf-8')

        # XML 형식의 API Response 를 읽기 위한 ElementTree
        # XMl 형식이지만 type 은 string 이므로 fromstring 메소드 사용
        tree = ET.ElementTree(ET.fromstring(result))
        root = tree.getroot()  # 최상위 노드 root

        # print(root.text)
        # for child in root[1][1]:
        #     print(child.tag, child.text)
        # print(root.text)

        items = root[1][1]
        for item in items:
            row = dict()
            for value in item:
                row[value.tag] = value.text
                # print(value.tag, value.text)

            df = df.append(row, ignore_index=True)

        # print(station_code_csv[station_code_csv["지점"] == s_code]["지점명"].values[0])

        # print(df.info)

    # 내가 정한 col 만 가져옴
    df = df[attributes]

    # col 명 한글로 바꿈
    df.columns = columns

    # print(df.columns)
    # print(df)

    df.to_csv(file_name, encoding="utf-8", index=False)


if __name__ == "__main__":
    # serviceKey, getWthrDataList, file_name
    serviceKey = "p3RjGK2spO6S8g%2Bc7oh4wF2EbfQBUbljSP1wLcCY%2BbfQBwQDSWqMFjgmnBlfSeNTRk9%2Fa5peMnYbRNvXMqSGtQ%3D%3D"

    start_ymd = "20010101"
    end_ymd = "20191231"

    file_name = "../weather_data/일기상자료_" + start_ymd + "_" + end_ymd + ".csv"

    # OutlierStatistics_to_csv(serviceKey, file_name, start_ymd, end_ymd)

    # 관측 지점 코드
    station_code_csv = pd.read_csv("관측지점코드.csv", sep="\t")

    station_code = station_code_csv["지점"]

    for s_code in station_code[:]:
        # file_name 설정
        station_name = station_code_csv.loc[station_code_csv["지점"] == s_code, "지점명"].values[0]

        start_year = 2001
        end_year = 2019

        print(station_code_csv[station_code_csv["지점"] == s_code].index)

        weatherData_to_csv_byStation(serviceKey, station_name, start_year, end_year)

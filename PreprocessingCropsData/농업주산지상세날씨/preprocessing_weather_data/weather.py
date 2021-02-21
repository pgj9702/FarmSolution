from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import urllib
import xml.etree.ElementTree as ET
import pandas as pd
import datetime


# 작물별 데이터를 csv 로 저장 (2001-2019 까지 모든 날짜, 모든 지역)
def DayStatistics_to_csv_byCrop(serviceKey, PA_CROP_SPE_ID, file_name):

    # url
    url = "http://apis.data.go.kr/1360000/FmlandWthrInfoService/getDayStatistics"

    # attributes
    attributes = [
        "areaId", "areaName", "dayAvgRhm", "dayAvgTa", "dayAvgWs",
        "dayMaxTa", "dayMinRhm", "dayMinTa", "daySumRn", "daySumSs",
        "paCropName", "paCropSpeId", "paCropSpeName", "wrnCd", "wrnCount",
        "ymd"
    ]

    columns = ['지역 아이디', '지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속',
               '일 최고기온', '일 최저상대습도', '일 최저기온', '일 강수량', '일 누적일조시간',
               '작물 명', '작물별 특성아이디', '작물별 특성 이름', '특보 코드', '특보 발효 여부',
               '연월일']

    # 데이터 요청 시작 (진행 상황 표시)
    print("Start to get area_data, Crop Id :", PA_CROP_SPE_ID)

    df_for_storage = pd.DataFrame(columns=columns)
    df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")

    # 2001년 1월 1일부터 2019년 12월 31일까지 반복하는 while 문
    for year in range(2001, 2020):
        ST_YMD = "%s0101" % year
        ED_YMD = "%s1231" % year

        # request 의 pageNo
        # 페이지 1로 초기화
        pageNo = 1

        # 모든 페이지를 조회하는 while, 데이터가 없는 page 일 경우 종료
        while True:

            df = pd.DataFrame(columns=attributes)
            queryParams = '?' + urlencode({quote_plus('ServiceKey'): serviceKey,
                                           quote_plus('pageNo'): str(pageNo),
                                           quote_plus('dataType'): 'XML',
                                           quote_plus('numOfRows'): '15000',
                                           quote_plus('ST_YMD'): ST_YMD,
                                           quote_plus('ED_YMD'): ED_YMD,
                                           quote_plus('AREA_ID'): "999999999",
                                           quote_plus('PA_CROP_SPE_ID'): PA_CROP_SPE_ID})

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

            # resultMsg 가 NO_DATA 일 경우 pageNo 출력 후 종료
            if resultMsg == "NO_DATA":
                break

            # resultMsg 가 NORMAL_SERVICE 가 아닌 경우 (오류)
            elif resultMsg != "NORMAL_SERVICE":
                print("ERROR :", resultMsg)
                print("End")
                break

            # 최초 1회 실행, columns 만 존재하는 csv 파일 생성
            # elif pageNo == 1:
            #     df_for_storage = pd.DataFrame(columns=columns)
            #     df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")

            # resultMsg 가 NORMAL_SERVICE 인 경우 pageNo 출력 (진행 상황 표시)
            # print("Get area_data in %s ... ( pageNo" % date, pageNo, ")")

            # root 는 header(응답 정보) 와 body(데이터)로 구성
            # root[1] 은 body, root[1][1] 은 items (rows 를 가짐)
            for item in root[1][1]:
                res = dict()
                for element in item:
                    res[element.tag] = element.text

                df = df.append(res, ignore_index=True)

            # excel 파일에 이어서 저장
            df.to_csv(file_name, mode="a", header=False, index=False, encoding="utf-8-sig")

            # 페이지를 한 장씩 넘김
            pageNo += 1




# getDayStatistics 1년 단위로 Data 를 요청하는 함수
def DayStatistics_to_csv_yearly(serviceKey, year, AREA_ID, PA_CROP_SPE_ID, file_name):
    # request 의 pageNo
    pageNo = 1

    # request 의 시작일, 종료일
    ST_YMD = "%s0101" % year
    ED_YMD = "%s1231" % year
    year = int(year)
    Day_YMD = datetime.date(year, 1, 1)

    # 요청 url
    url = "http://apis.data.go.kr/1360000/FmlandWthrInfoService/getDayStatistics"

    # 결과 메세지
    resultMsg = ""

    # attributes
    attributes = [
        "areaId", "areaName", "dayAvgRhm", "dayAvgTa", "dayAvgWs",
        "dayMaxTa", "dayMinRhm", "dayMinTa", "daySumRn", "daySumSs",
        "paCropName", "paCropSpeId", "paCropSpeName", "wrnCd", "wrnCount",
        "ymd"
    ]

    columns = ['지역 아이디', '지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속',
               '일 최고기온', '일 최저상대습도', '일 최저기온', '일 강수량', '일 누적일조시간',
               '작물 명', '작물별 특성아이디', '작물별 특성 이름', '특보 코드', '특보 발효 여부',
               '연월일']

    # 데이터 요청 시작 (진행 상황 표시)
    print("Start to get area_data(DayStatistics) in", year)

    df_for_storage = pd.DataFrame(columns=columns)
    df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")

    # 1월 1일부터 12월 31일까지 반복하는 while 문
    while Day_YMD.year == year:

        # 모든 페이지를 조회하는 while, 데이터가 없는 page 일 경우 종료
        while True:
            # Response 를 저장할 DataFrame
            df = pd.DataFrame(columns=attributes)

            queryParams = '?' + urlencode({quote_plus('ServiceKey'): serviceKey,
                                           quote_plus('pageNo'): str(pageNo),
                                           quote_plus('dataType'): 'XML',
                                           quote_plus('numOfRows'): '100',
                                           quote_plus('ST_YMD'): Day_YMD,
                                           quote_plus('ED_YMD'): Day_YMD,
                                           quote_plus('AREA_ID'): AREA_ID,
                                           quote_plus('PA_CROP_SPE_ID'): PA_CROP_SPE_ID})

            rq = urllib.request
            body = rq.urlopen(url + queryParams)
            rq.get_method = lambda: 'GET'
            response_body = body.read()
            result = response_body.decode('utf-8')

            # XML 형식의 API Response 를 읽기 위한 ElementTree
            # XMl 형식이지만 type 은 string 이므로 fromstring 메소드 사용
            tree = ET.ElementTree(ET.fromstring(result))
            root = tree.getroot()   # 최상위 노드 root

            # resultMsg 태그를 읽어 NO_DATA 인지 확인
            resultMsg = root[0][1].text

            # resultMsg 가 NO_DATA 일 경우 pageNo 출력 후 종료
            if resultMsg == "NO_DATA":
                print("No area_data on pageNo", pageNo)
                print("End")
                break

            # resultMsg 가 NORMAL_SERVICE 가 아닌 경우 (오류)
            elif resultMsg != "NORMAL_SERVICE":
                print("ERROR :", resultMsg)
                print("End")
                break

            # 최초 1회 실행, columns 만 존재하는 csv 파일 생성
            # elif pageNo == 1:
            #     df_for_storage = pd.DataFrame(columns=columns)
            #     df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")

            # resultMsg 가 NORMAL_SERVICE 인 경우 pageNo 출력 (진행 상황 표시)
            print("Get area_data ... ( pageNo", pageNo, ")")

            # root 는 header(응답 정보) 와 body(데이터)로 구성
            # root[1] 은 body, root[1][1] 은 items (rows 를 가짐)
            for item in root[1][1]:
                res = dict()
                for element in item:
                    res[element.tag] = element.text

                df = df.append(res, ignore_index=True)

            # excel 파일에 이어서 저장
            df.to_csv(file_name, mode="a", header=False, index=False, encoding="utf-8-sig")

            # 페이지를 한 장씩 넘김
            pageNo += 1

        # 날짜를 하루 넘김, 페이지 1로 초기화
        Day_YMD = Day_YMD + datetime.timedelta(days=1)
        pageNo = 1


if __name__ == "__main__":

    # 파라미터
    decode_key = unquote(
        "p3RjGK2spO6S8g%2Bc7oh4wF2EbfQBUbljSP1wLcCY%2BbfQBwQDSWqMFjgmnBlfSeNTRk9%2Fa5peMnYbRNvXMqSGtQ%3D%3D")

    year = "2019"
    AREA_ID = "999999999"   # 지역 ID, 999999999 일 경우 모든 지역 조회
    PA_CROP_SPE_ID = "PA999999"   # 작물특성 ID, PA999999 일 경우 모든 작물 조회
    file_name = "weather_data/test2%s.csv" % year

    # DayStatistics_to_csv_yearly(decode_key, year, AREA_ID, PA_CROP_SPE_ID, file_name)

    # for year in [str(i) for i in range(2006, 2021)]:
    #     file_name = "weather_data/농업주산지상세날씨_일통계_%s.csv" % year
    #     DayStatistics_to_csv_yearly(decode_key, year, AREA_ID, PA_CROP_SPE_ID, file_name)

    # 작물별 데이터 저장
    crops_df = pd.read_csv("../작물목록.csv", encoding='cp949')

    for crop_id, crop_name, crop_kind in zip(crops_df["작물별 특성 아이디"], crops_df["작물명"], crops_df["세부분류"]):

        file_name = "../preprocessed_weather_data/%s_%s_날씨.csv" % (crop_name, crop_kind)

        DayStatistics_to_csv_byCrop(decode_key, crop_id, file_name)



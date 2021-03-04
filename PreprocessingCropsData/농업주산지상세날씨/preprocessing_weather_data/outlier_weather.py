import urllib
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd
import xml.etree.ElementTree as ET


# 날씨 데이터를 csv 로 저장 (2017-12-21 ~ 24 까지 모든 날짜, 모든 지역)
def OutlierStatistics_to_csv(serviceKey, file_name, start_ymd, end_ymd):

    # 관측 지점 코드
    station_code_csv = pd.read_csv("관측지점코드.csv", sep="\t")

    print(station_code_csv)

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

        queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKey,
                                        quote_plus('pageNo') : '1',
                                        quote_plus('numOfRows') : '10',
                                        quote_plus('dataType') : 'XML',
                                        quote_plus('dataCd') : 'ASOS',
                                        quote_plus('dateCd') : 'DAY',
                                        quote_plus('startDt') : start_ymd,
                                        quote_plus('endDt') : end_ymd,
                                        quote_plus('stnIds') : s_code })

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

        print(station_code_csv[station_code_csv["지점"] == s_code]["지점명"].values[0])

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

    OutlierStatistics_to_csv(serviceKey, file_name, start_ymd, end_ymd)
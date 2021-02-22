import urllib
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd
import xml.etree.ElementTree as ET


# 날씨 데이터를 csv 로 저장 (2017-12-21 ~ 24 까지 모든 날짜, 모든 지역)
def OutlierStatistics_to_csv(serviceKey, file_name):

    # url
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'

    # attributes
    attributes = [
        "stnNm", "avgRhm", "avgTa", "avgWs",
        "maxTa", "minRhm", "minTa", "sumRn",
        "sumSsHr", "tm "
    ]

    columns = ['지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속',
               '일 최고기온', '일 최저상대습도', '일 최저기온', '일 강수량',
               '일 누적일조시간', '연월일']

    # 데이터 요청 시작 (진행 상황 표시)
    print("Start to get area_data, Country Id :")

    # df_for_storage = pd.DataFrame(columns=columns)
    # df_for_storage.to_csv(file_name, index=False, encoding="utf-8-sig")


    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKey,
                                    quote_plus('pageNo') : '1',
                                    quote_plus('numOfRows') : '10',
                                    quote_plus('dataType') : 'XML',
                                    quote_plus('dataCd') : 'ASOS',
                                    quote_plus('dateCd') : 'DAY',
                                    quote_plus('startDt') : '20171221',
                                    quote_plus('endDt') : '20171224',
                                    quote_plus('stnIds') : '108' })

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
    print(root.text)
    for child in root[0]:
        print(child.tag, child.text)


if __name__ == "__main__":
    # serviceKey, getWthrDataList, file_name
    serviceKey = "p3RjGK2spO6S8g%2Bc7oh4wF2EbfQBUbljSP1wLcCY%2BbfQBwQDSWqMFjgmnBlfSeNTRk9%2Fa5peMnYbRNvXMqSGtQ%3D%3D"

    file_name = ""
    OutlierStatistics_to_csv(serviceKey, file_name)



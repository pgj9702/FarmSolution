import request_api
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import urllib
import xml.etree.ElementTree as ET
import pandas as pd
import datetime

if __name__ == "__main__":

    # url
    url = "http://apis.data.go.kr/1360000/FmlandWthrInfoService/getDayStatistics"

    # 파라미터
    decode_key = unquote(
        "p3RjGK2spO6S8g%2Bc7oh4wF2EbfQBUbljSP1wLcCY%2BbfQBwQDSWqMFjgmnBlfSeNTRk9%2Fa5peMnYbRNvXMqSGtQ%3D%3D")

    year = "2019"
    AREA_ID = "999999999"   # 지역 ID, 999999999 일 경우 모든 지역 조회
    PA_CROP_SPE_ID = "PA999999"   # 작물특성 ID, PA999999 일 경우 모든 작물 조회
    file_name = "weather_data/test2%s.csv" % year

    # attributes
    attributes = [
        "areaId", "areaName", "dayAvgRhm", "dayAvgTa", "dayAvgWs",
        "dayMaxTa", "dayMinRhm", "dayMinTa", "daySumRn", "daySumSs",
        "paCropName", "paCropSpeId", "paCropSpeName", "wrnCd", "wrnCount",
        "ymd"
    ]

    pageNo = 1

    Day_YMD = "20171222"

    weather_api = request_api.RequestAPI(url)

    params = {'ServiceKey': decode_key, 'pageNo': str(pageNo), 'dataType': 'XML',
              'numOfRows': '100', 'ST_YMD': Day_YMD, 'ED_YMD': Day_YMD,
              'AREA_ID': AREA_ID, 'PA_CROP_SPE_ID': PA_CROP_SPE_ID}

    weather_api.request_api(params)

    root = weather_api.root

    # resultMsg 태그를 읽어 NO_DATA 인지 확인
    resultMsg = root[0][1].text

    print(resultMsg)

    # df = pd.DataFrame(columns=attributes)

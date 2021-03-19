from numpy import nan as NA
import pandas as pd
import numpy as np
import urllib
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd
import xml.etree.ElementTree as ET
import json
import requests


def web_request(method_name, url, dict_data, is_urlencoded=True):
    """Web GET or POST request를 호출 후 그 결과를 dict형으로 반환 """
    method_name = method_name.upper()  # 메소드이름을 대문자로 바꾼다
    if method_name not in ('GET', 'POST'):
        raise Exception('method_name is GET or POST plz...')

    if method_name == 'GET':  # GET방식인 경우
        response = requests.get(url=url, params=dict_data)
    elif method_name == 'POST':  # POST방식인 경우
        if is_urlencoded is True:
            response = requests.post(url=url, data=dict_data,
                                     headers={'Content-Type': 'application/x-www-form-urlencoded'})
        else:
            response = requests.post(url=url, data=json.dumps(dict_data), headers={'Content-Type': 'application/json'})

    dict_meta = {'status_code': response.status_code, 'ok': response.ok, 'encoding': response.encoding,
                 'Content-Type': response.headers['Content-Type']}

    print(response.text)
    print(type(response.json()))

    if 'json' in str(response.headers['Content-Type']):  # JSON 형태인 경우
        return {**dict_meta, **response.json()}
    else:  # 문자열 형태인 경우
        return {**dict_meta, **{'text': response.text}}


# XML 형식의 API Response 를 읽기 위한 ElementTree
# XMl 형식이지만 type 은 string 이므로 fromstring 메소드 사용
# tree = ET.ElementTree(ET.fromstring(result))
# root = tree.getroot()  # 최상위 노드 root

# POST방식 호출 테스트('Content-Type': 'application/x-www-form-urlencoded')
url  = 'http://127.0.0.1:8000/crops/predict/' # 접속할 사이트주소 또는 IP주소를 입력한다
data = {'uid': 'good'}          # 요청할 데이터
response = web_request(method_name='POST', url=url, dict_data=data, is_urlencoded=True)

if response['ok'] == True:
    print(response['prediction'])
    # 성공 응답 시 액션
else:
    pass
    # 실패 응답 시 액션
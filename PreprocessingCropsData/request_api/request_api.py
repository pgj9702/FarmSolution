from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import urllib
import xml.etree.ElementTree as ET
import pandas as pd
import datetime


class RequestAPI:

    url: str
    root: ET.Element    # response 의 xml root

    def __init__(self, url):
        self.url = url

    def request_api(self, params: dict):

        queryParams = '?' + urlencode({quote_plus(k): v for k, v in params.items()})

        rq = urllib.request
        body = rq.urlopen(self.url + queryParams)
        rq.get_method = lambda: 'GET'
        response_body = body.read()
        result = response_body.decode('utf-8')

        # XML 형식의 API Response 를 읽기 위한 ElementTree
        # XMl 형식이지만 type 은 string 이므로 fromstring 메소드 사용
        tree = ET.ElementTree(ET.fromstring(result))
        root = tree.getroot()  # 최상위 노드 root

        self.root = root

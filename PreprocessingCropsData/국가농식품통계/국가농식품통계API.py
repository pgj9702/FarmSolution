# Python 샘플 코드 #

# from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import urllib.request

# http://kass.mafra.go.kr/kass/ka/ss/openapi/openApiSvcMain.do?upMenuCd=3003&menuCd=3031

url = 'http://kass.mafra.go.kr/kass/ws/data'
url = "http://apis.data.go.kr/1360000/FmlandWthrInfoService/getDayStatistics"

decode_key = unquote("AaensNBsqKP0tp1wEpSiZk7AtSSsyo5uH5YUvNQt8VI%2Bfa7JgKUhi02miQ2AoRtSs6IJEtN5O7Pqta0aQpiCLg%3D%3D")

queryParams = '?' + urlencode({ quote_plus('accessToken') : decode_key,
                                quote_plus('responseType') : 'xml',
                                quote_plus('tbType') : '001', quote_plus('aprvSn') : '114016', quote_plus('tbYear') : '2019', quote_plus('itemCd1') : 'all'})

print('decode_key', decode_key)

rq = urllib.request
body = rq.urlopen(url + queryParams)
rq.get_method = lambda: 'GET'
response_body = body.read()
result = response_body.decode('utf-8')

print(result)



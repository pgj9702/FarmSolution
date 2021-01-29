from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import urllib
import xml.etree.ElementTree as ET
import pandas as pd

# getDayStatistics 1년 단위로 Data 를 요청하는 함수
def getSoilCropFitInfo_DataFrame(ServiceKey, serviceKey):

    # 요청 url
    url = "http://apis.data.go.kr/1390802/SoilEnviron/SoilFitStat/getSoilCropFitInfo"

    # 결과 메세지
    resultMsg = ""

    # attributes
    attributes = [
        "bjd_Code",
        "bjd_Nm",
        "soil_Crop_Code",
        "soil_Crop_Nm",
        "high_Suit_Area",
        "suit_Area",
        "low_Suit_Area",
        "poss_Area",
        "etc_Area",
    ]

    columns = ["법정동코드", "법정동명", "토양적성작물ID", "토양저성작물명",
               "최적지면적", "적지면적", "가능지면적", "저위생산지면적", "기타면적"]

    # DataFrame
    df = pd.DataFrame(columns=attributes)

    # 법정동코드 파일 읽기
    area_code_data = pd.read_csv("법정동코드 전체자료.txt", delimiter='\t', encoding='utf-8')

    # 작물코드 파일 읽기
    crop_code_data = pd.read_csv("작물코드.csv", encoding='utf-8')

    for area_code in area_code_data.iterrows():

        for crop_code in crop_code_data.iterrows():

            queryParams = '?' + urlencode(
                {quote_plus('ServiceKey'): "=서비스키",
                 quote_plus('serviceKey'): serviceKey,
                 quote_plus('BJD_Code'): area_code[1]["법정동코드"],
                 quote_plus('soil_Crop_Code'): crop_code[1]["코드"]})

            # "result_Code",
            # "result_Msg",

            rq = urllib.request
            body = rq.urlopen(url + queryParams)
            rq.get_method = lambda: 'GET'
            response_body = body.read()
            result = response_body.decode('utf-8')

            tree = ET.ElementTree(ET.fromstring(result))
            root = tree.getroot()

            print(area_code[1]["법정동코드"], crop_code[1]["코드"], "test")
            print(result)

            for i in root.items():
                print(i)

        #     # resultMsg 태그를 읽어 NO_DATA 인지 확인
        #     resultMsg = root[0][1].text
        #
        #     print(resultMsg)
        #
        #     if resultMsg == "NO_DATA":
        #         break
        #
        #     # root 는 header 와 body로 구성
        #     # root[1] 은 body, root[1][1] 은 items
        #     for item in root[1][1]:
        #         res = dict()
        #         for element in item:
        #             res[element.tag] = element.text
        #
        #         df = df.append(res, ignore_index=True)
        #
        # df.columns = columns
        #
        # return df



if __name__ == "__main__":

    # 파라미터
    decode_key = unquote(
        "AaensNBsqKP0tp1wEpSiZk7AtSSsyo5uH5YUvNQt8VI%2Bfa7JgKUhi02miQ2AoRtSs6IJEtN5O7Pqta0aQpiCLg%3D%3D")

    # getSoilCropFitInfo_DataFrame(decode_key01, decode_key02)

    #
    # if not df.empty:
    #     print(df.info)
    #     df.to_excel("토양적성_data/농업주산지상세날씨.xlsx")



    # 법정동코드 파일 읽기
    area_code_data = pd.read_csv("법정동코드 전체자료.txt", delimiter='\t', encoding='utf-8')

    # 작물코드 파일 읽기
    crop_code_data = pd.read_csv("작물코드.csv", encoding='utf-8')

    url = "http://apis.data.go.kr/1390802/SoilEnviron/SoilFitStat/getSoilCropFitInfo"

    queryParams = '?' + urlencode(
        {quote_plus('serviceKey'): decode_key,
         quote_plus('BJD_Code'): "1100000000",
         quote_plus('soil_Crop_Code'): crop_code_data["코드"][0]})

    # "result_Code",
    # "result_Msg",

    rq = urllib.request
    body = rq.urlopen(url + queryParams)
    rq.get_method = lambda: 'GET'
    response_body = body.read()
    result = response_body.decode('utf-8')

    tree = ET.ElementTree(ET.fromstring(result))
    root = tree.getroot()

    print(result)

    for i in root.items():
        print(i)

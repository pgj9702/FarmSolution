import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd


def typhoon():

    url = 'https://www.weather.go.kr/weather/typoon/statistic.jsp'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.select('tbody')
        # bs4.element.Tag.children

        table = table[1]


        df = pd.DataFrame()

        column = ['연월일', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '합계']

        df = pd.DataFrame(columns=column)

        for tr_table in table:
            for sell in tr_table:
                if type(sell) is bs4.element.Tag:
                    if sell.tag == "th":
                        year = sell.text

                    elif sell.tag == "td":
                        value = sell.text







                    #print(sell)


        # if table.text[0]

        # titles = div.select('div>table')
        # for table in titles:
        #     print(table.get_text())

    else:
        print(response.status_code)

    # df = pd.DataFrame()
    #
    # df.to_csv(filename)
    #
    # return df

#
if __name__ == "__main__":
    typhoon()
#     df = typhoon(2001, 2020, "/경로/파일명.csv")






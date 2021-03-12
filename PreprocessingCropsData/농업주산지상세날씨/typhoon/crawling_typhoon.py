import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
from pyparsing import col


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

        values = [1 for _ in range(14)]

        diction = {key: value for key, value in zip(column, values)}

        df = df.append(diction, ignore_index=True)

        row_count = -1
        col_count = 1

        for tr_table in table:
            for sell in tr_table:
                if type(sell) is bs4.element.Tag:
                    # print(sell, sell.text, sell.name)
                    if sell.name == "th":
                        year = sell.text
                        col_count = 1
                        row_count += 1
                        df.loc[row_count, "연월일"] = year

                    elif sell.name == "td":
                        value = sell.text

                        df.iloc[row_count, col_count] = value
                        col_count += 1

        print(df)
        
        # 2018 년도는 직접 작성해야함

        df = df.replace(" ", "")
        #df = df.replace("\xa0", "")

        df.to_csv("typhoon.csv", encoding="utf-8", index=False)







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






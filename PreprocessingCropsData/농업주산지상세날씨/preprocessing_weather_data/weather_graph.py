import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os

if __name__ == "__main__":

    # 한글 폰트 설정
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # 음수 부호 설정
    rc('axes', unicode_minus=False)

    # None, 제외할 col, log, 특성곱

    # 읽을 파일 경로
    input_file_path = "../preprocessed_weather_data/"

    # 지점별 데이터 누락, 중복 검토
    stations_df = pd.read_csv("관측지점코드.csv", sep="\t")

    station_name = "춘천"

    input_file_name = "일기상자료_%s_2001_2019.csv" % station_name

    weather_df = pd.read_csv(input_file_path + input_file_name, low_memory=False)

    print(station_name)
    for i, row in weather_df.loc[:, ["시간", "일 최심적설"]].iterrows():
        print(row)

    weather_df.hist(bins=50, figsize=(18, 16))
    plt.show()


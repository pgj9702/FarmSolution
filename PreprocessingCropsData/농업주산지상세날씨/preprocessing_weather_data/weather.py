import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    # None, 제외할 col, log, 특성곱

    # 누락/ 중복 기록
    error_list = []

    # 지점별 데이터 누락, 중복 검토
    stations_df = pd.read_csv("관측지점코드.csv", sep="\t")

    # 읽을 파일 경로
    input_file_path = "../weather_data/"

    # 파일 저장 경로
    path_to_save = "../preprocessed_weather_data/"

    for station_id, station_name in zip(stations_df["지점"], stations_df["지점명"]):

        # 읽을 파일
        input_file_name = "일기상자료_%s_2001_2019.csv" % station_name

        weather_df = pd.read_csv(input_file_path + input_file_name, low_memory=False)

        col_del = ["최저 기온 시각", "최대 기온 시각", "10분 최다강수량 시각", "1시간 최다 강수량 시각",
                   "최대 순간 풍속 풍향", "최대 순간풍속 시각", "최대 풍속 풍향", "최대 풍속 시각",
                   "최대 풍향", "평균 상대습도 시각", "최고 해면 기압", "최고 해면기압 시각",
                   "최저 해면기압", "최저 해면기압 시각", "평균 해면기압", "1시간 최다 일사량 시각",
                   "일 최심신적설 시각", "일 최심적설 시각", "합계 3시간 신적설", "평균 전운량",
                   "평균 중하층운량", "합계 대형증발량", "합계 소형증발량", "9-9강수",
                   "일기현상", "안개 계속 시간"]

        weather_df.drop(col_del, axis=1, inplace=True)

        # print(station_name)

        # row 의 첫 행 weather_df.loc[0, "시간"]
        first_date = weather_df.loc[0, "시간"]
        # print(first_date)

        first_ymd = first_date.split("-")
        
        if first_ymd[1] != "01" or first_ymd[2] != "01":
            idx = weather_df[weather_df["시간"].str.contains(first_ymd[0])].index
            weather_df.drop(idx, inplace=True)

        weather_df.reset_index(inplace=True, drop=True)

        # 2001 년도 자료가 없으면 넘김
        if len(weather_df) != 0 and first_date[:4] == "2001":
            first_date = weather_df.loc[0, "시간"]
            # print("re", first_date)
        else:
            continue
            # print("null df")

        # 전날과 앞날의 중간값으로 None 값 처리 (평균 기온, 최저 기온, 최고 기온)
        weather_df["평균 기온"].interpolate(inplace=True)
        weather_df["최저 기온"].interpolate(inplace=True)
        weather_df["최고 기온"].interpolate(inplace=True)

        # fillna : "일 최심신적설", "일 최심적설"
        # 적설량은 겨울에만 측정함, 그 외 Nan 으로 처리 됨
        weather_df["일 최심신적설"].fillna(0, inplace=True)
        weather_df["일 최심적설"].fillna(0, inplace=True)

        # 그 외의 특성들은 센서 오류 등으로 측정하지 못하여 생긴 None 으로 결측치를 대체하기 어려움
        # 데이터셋에서는 None 을 제외한 값들로 계산하여 구성

        # 저장할 파일 명
        # output_file_name = "일기상자료_%s_%s_2019.csv" % (station_name, first_date[:4])

        print(station_id, station_name, "일기상자료")

        # print("평균 기온 결측일", len(null_rows), "전체 row 비율", int( len(null_rows) / len(weather_df) * 100))

        # print(null_len.loc[:, ["시간", "일강수량", "평균 상대습도"]])

        # print(null_rows)2010-08-29

        # weather_df["일강수량"].hist(bins=100, figsize=(20,15))
        # plt.show()

        output_file_name = "일기상자료_%s_%s_2019.csv" % (station_name, first_date[:4])
        weather_df.to_csv(path_to_save + output_file_name, index=False, encoding="utf-8-sig")


    # print(error_list)

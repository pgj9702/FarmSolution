import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # None, 제외할 col, log, 특성곱

    # 누락/ 중복 기록
    error_list = []

    # 지점별 데이터 누락, 중복 검토
    stations_df = pd.read_csv("관측지점코드.csv", sep="\t")

    for station_id, station_name in zip(stations_df["지점"], stations_df["지점명"]):

        file_name = "../weather_data/일기상자료_%s_2001_2019.csv" % station_name

        weather_df = pd.read_csv(file_name, low_memory=False)

        aver_temp = weather_df["일강수량"]

        null_values = aver_temp.isnull()

        null_len = weather_df[null_values]

        test_df = null_len.loc[:, ["10분 최다강수량 시각", "1시간 최다강수량", "1시간 최다 강수량 시각", "일강수량"]]

        # print(weather_df["9-9강수"])

        print(station_id, station_name, "일기상자료")

        print("일강수량 결측일", len(null_len), "전체 row 비율", int( len(null_len) / len(weather_df) * 100))

        weather_df["일강수량"].hist(bins=100, figsize=(20,15))
        plt.show()

        # 1. 각 열 별 결측치 체크
        # check_nan = weather_df.T.isnull().values
        #
        # print("row 수 :", len(weather_df))
        #
        # print("결측치가 존재하는 column :", end=" ")
        #
        # for col_idx in range(len(weather_df.columns)):
        #     if check_nan[col_idx].any():
        #         print(weather_df.columns[col_idx], end=" ")
        #
        # print()
        #
        # # 지역별 누락 날짜 확인
        # day_list = list(weather_df["시간"])
        #
        # day_list = [dt.datetime.strptime(day, "%Y-%m-%d") for day in day_list]
        #
        # print("day_list len :", len(day_list), day_list[0], "~", day_list[len(day_list) - 1])
        #
        # for idx in range(len(day_list) - 1):
        #     if day_list[idx] == day_list[idx + 1]:
        #         print("중복 발생", day_list[idx], day_list[idx + 1])
        #         error_list.append({"발생일1": day_list[idx], "발생일2": day_list[idx + 1]})
        #     elif day_list[idx] != day_list[idx + 1] - dt.timedelta(days=1) and \
        #             day_list[idx] != day_list[idx + 1]:
        #         print("누락 발생", day_list[idx], day_list[idx + 1])
        #         error_list.append({"지점": station_name,"발생일1": day_list[idx], "발생일2": day_list[idx + 1]})

        print("종료")

    print(error_list)

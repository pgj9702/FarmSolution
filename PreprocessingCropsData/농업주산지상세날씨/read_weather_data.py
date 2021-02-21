import pandas as pd
import numpy as np
import datetime
from matplotlib import pyplot as plt


# 데이터를 읽기 위한 클래스
class ReadData:

    def __init__(self):
        pass

    # csv 파일 읽기
    def read_csv(self, path, file):
        df = pd.read_csv(path + file, low_memory=False)

        return df

    # 농업주산지상세날씨
    def read_weather_info(self):
        pass

    # 토양적성통계
    def read_soil_info(self):
        pass

    # 농작물 생산량
    def read_crop_production_info(self):
        pass

    # 농업면적
    def read_farmland_area_info(self):
        pass

    # 데이터셋 준비
    def set_data(self):
        pass


def func1():

    # ReadData 클래스 객체 생성
    read_data = ReadData()

    weather_info_path = "weather_data/"
    weather_info_file = "농업주산지상세날씨_일통계_2001.csv"

    weather_df = read_data.read_csv(weather_info_path, weather_info_file)

    print(weather_df.columns)

    for year in range(2019, 2020):

        weather_info_file = "testDaily%d.csv" % year
        weather_df = read_data.read_csv(weather_info_path, weather_info_file)

        # 1. 지역 이름
        # 지역 수 (중복 제거)
        area_count = len(set(weather_df["지역 이름"]))

        # 지역 이름 list (중복 제거)
        area_list = list(set(weather_df["지역 이름"]))

        # 2. 특보 코드
        # 특보 발생 수 (nan 제외)
        warn_count = weather_df["특보 코드"].count()

        # 발생한 특보 코드 list
        warn_code_list = list(set(weather_df["특보 코드"]))  # 중복 제거
        warn_code_list = [x for x in warn_code_list if str(x) != "nan"]  # nan 제외

        # 3. 각 열 별 결측치 체크
        check_nan = weather_df.T.isnull().values

        print(year, "년도 농업주산지상세날씨 정보")

        print("row 수 :", len(weather_df))

        print("지역 수 :", area_count, "\t지역 이름 :", area_list[: area_count if area_count < 10 else 10])

        print("발생한 특보 코드 :", warn_code_list, "\t특보 발생 수 :", warn_count)

        print("결측치가 존재하는 column :", end=" ")

        for col_idx in range(len(weather_df.columns)):
            if check_nan[col_idx].any():
                print(weather_df.columns[col_idx], end=" ")

        print()

        # 지역, 작물별 누락 날짜 확인
        print("지역, 작물 별 누락 일자 확인 중 ...")
        for area in area_list:
            area_df = weather_df[weather_df["지역 이름"] == area]
            cropId_list = list(set(area_df["작물별 특성아이디"]))

            for cropId in cropId_list:

                area_crop_df = area_df[area_df["작물별 특성아이디"] == cropId]

                day_list = list(area_crop_df["연월일"])

                day_list = [datetime.datetime.strptime(day, "%Y-%m-%d %H:%M:%S") for day in day_list]

                day_list.sort()

                for idx in range(len(day_list) - 1):
                    print(day_list[idx], day_list[idx + 1])
                    if day_list[idx] < day_list[idx + 1] - datetime.timedelta(days=1) and \
                            list(area_crop_df["특보 코드"])[idx] == list(area_crop_df["특보 코드"])[idx + 1]:
                        print(area, cropId)
                        print(day_list[idx], day_list[idx + 1])

                # print("작물", crop, " 의 날짜 결측치")

        print("종료")


if __name__ == "__main__":

    # 누락/ 중복 기록
    error_list = []

    # 작물별 데이터 누락, 중복 검토
    crops_df = pd.read_csv("작물목록.csv", encoding='cp949')

    for crop_id, crop_name, crop_kind in zip(crops_df["작물별 특성 아이디"], crops_df["작물명"], crops_df["세부분류"]):

        file_name = "preprocessed_weather_data/%s_%s_날씨.csv" % (crop_name, crop_kind)

        crop_weather_df = pd.read_csv(file_name)

        # 1. 지역 이름

        # 지역 아이디 list (중복 제거)
        area_list = list(set(crop_weather_df["지역 아이디"]))

        # 지역 수
        area_count = len(area_list)

        # 2. 특보 코드
        # 특보 발생 수 (nan 제외)
        warn_count = crop_weather_df["특보 코드"].count()

        # 발생한 특보 코드 list
        warn_code_list = list(set(crop_weather_df["특보 코드"]))  # 중복 제거
        warn_code_list = [x for x in warn_code_list if str(x) != "nan"]  # nan 제외

        # 3. 각 열 별 결측치 체크
        check_nan = crop_weather_df.T.isnull().values

        print(crop_name, crop_kind, "농업주산지상세날씨 정보")

        print("row 수 :", len(crop_weather_df))

        print("지역 수 :", area_count, "\t지역 이름 :", area_list[: area_count if area_count < 10 else 10])

        print("발생한 특보 코드 :", warn_code_list, "\t특보 발생 수 :", warn_count)

        print("결측치가 존재하는 column :", end=" ")

        for col_idx in range(len(crop_weather_df.columns)):
            if check_nan[col_idx].any():
                print(crop_weather_df.columns[col_idx], end=" ")

        print()

        # 지역별 누락 날짜 확인
        print("지역별 누락 일자 확인 중 ...")
        for area in area_list:
            area_df = crop_weather_df[crop_weather_df["지역 아이디"] == area]

            day_list = list(area_df["연월일"])

            day_list = [datetime.datetime.strptime(day, "%Y-%m-%d %H:%M:%S") for day in day_list]

            print("지역 :", area, "day_list len :", len(day_list), day_list[0], day_list[len(day_list)-1])

            area_warn_list = list(area_df["특보 코드"])

            print(day_list)

            for idx in range(len(day_list) - 1):
                if day_list[idx] == day_list[idx + 1] and area_warn_list[idx] == area_warn_list[idx + 1]:
                    print("중복 발생", area, "지역 아이디", day_list[idx], day_list[idx + 1])
                    error_list.append({"지역 아이디": area, "발생일1": day_list[idx], "발생일2": day_list[idx + 1]})
                elif day_list[idx] != day_list[idx + 1] - datetime.timedelta(days=1) and \
                        day_list[idx] != day_list[idx + 1]:
                    print("누락 발생", area, "지역 아이디", day_list[idx], day_list[idx + 1])
                    error_list.append({"지역 아이디": area, "발생일1": day_list[idx], "발생일2": day_list[idx + 1]})

            # print("작물", crop, " 의 날짜 결측치")

        print("종료")

    print(error_list)
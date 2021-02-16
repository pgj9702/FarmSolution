import pandas as pd
import os


def preprocessing_datasets():
    weather_file_list = os.listdir("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data")

    weather_data = pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/감귤_-_날씨.csv")

    print(weather_data)


def func(x):
    print(x)

if __name__ == "__main__":
    # preprocessing_datasets()

    area_code = pd.read_csv("법정동코드 전체자료.txt", sep="\t")

    area_name_list = area_code["법정동명"].str.split()

    idx_list = []

    for i, v in area_name_list.items():
        if len(v) == 1:
            idx_list.append(i)

    sido_code = area_code.iloc[idx_list, :]
    sido_code = sido_code[sido_code["폐지여부"] == "존재"]

    print(sido_code)

    weather_data = pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/감귤_-_날씨.csv")

    print(weather_data)

    print(weather_data.columns)

    weather_df_columns = ['지역 아이디', '지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속', '일 최고기온', '일 최저상대습도',
       '일 최저기온', '일 강수량', '일 누적일조시간', '작물 명', '작물별 특성아이디', '작물별 특성 이름',
       '특보 코드', '특보 발효 여부', '연월일']

    col_to_use = ['지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속', '일 최고기온', '일 최저상대습도',
       '일 최저기온', '일 강수량', '일 누적일조시간', '특보 코드', '특보 발효 여부', '연월일']


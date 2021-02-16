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

    print(area_code.columns)

    area_name_list = area_code["법정동명"].str.split()

    print(area_name_list.apply(func))


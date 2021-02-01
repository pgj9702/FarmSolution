# 상위 디렉토리의 모듈 path 추가
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PreprocessingCropsData.Preprocessing import preprocess_csv

import pandas as pd


def preprocess_area_df(area_df: pd.DataFrame) -> pd.DataFrame:
    return area_df


if __name__ == "__main__":

    crops_list = ['봄무', '고랭지무', '가을무', '겨울무', '당근',
                  '봄배추', '고랭지배추', '가을배추', '겨울배추', '시금치',
                  '양배추', '고추', '마늘', '대파', '쪽파', '양파', '생강']

    columns_list = ['시도별', '2001 년', '2002 년', '2003 년', '2004 년', '2005 년',
                    '2006 년', '2007 년', '2008 년', '2009 년', '2010 년', '2011 년',
                    '2012 년', '2013 년', '2014 년', '2015 년', '2016 년', '2017 년',
                    '2018 년', '2019 년', '2020 년']

    input_file = "area_data/노지_채소_재배면적_2001_2020.csv"
    output_file = "preprocessedData/무_봄_면적.csv"

    # preprocess_csv()

    df = pd.read_csv(input_file, encoding="euc-kr")

    crop_area_df = df[(df["항목"] == crops_list[0]) & (df["종류별"] == "합계")]

    crop_area_df = crop_area_df.loc[:, columns_list]

    print(crop_area_df)

    preprocess_csv

    # print(crop_area_df.columns)

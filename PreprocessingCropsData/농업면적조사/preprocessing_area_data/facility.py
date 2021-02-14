import pandas as pd


def preprocess(area_df: pd.DataFrame, crop: str) -> pd.DataFrame:
    area_df = area_df[(area_df["항목"] == crop) & (area_df["종류별"] == "합계")]

    area_df = area_df.loc[:, columns_list]

    # 결측값은 0 으로 설정
    area_df = area_df.fillna(0)

    # '2001 년' 형식의 col 명을 '2001' 로 수정
    area_df.columns = [col.split(' ')[0] for col in area_df.columns]

    return area_df


if __name__ == "__main__":

    columns_list = ['시도별', '2001 년', '2002 년', '2003 년', '2004 년', '2005 년',
                    '2006 년', '2007 년', '2008 년', '2009 년', '2010 년', '2011 년',
                    '2012 년', '2013 년', '2014 년', '2015 년', '2016 년', '2017 년',
                    '2018 년', '2019 년', '2020 년']

    input_path = "../area_data/"
    output_path = "../preprocessed_area_data/"

    facility_input_file = "시설작물_재배면적_2001_2020.csv"

    facility_list = []

    facility_output_file_list = []

    # df = pd.read_csv(input_path + facility_input_file, encoding="euc-kr")
    #
    # for crop, output_file in zip(facility_list, facility_output_file_list):
    #     crop_area_df = preprocess(df, crop)
    #
    #     crop_area_df.to_csv(output_path + output_file, index=False, encoding="utf-8-sig")

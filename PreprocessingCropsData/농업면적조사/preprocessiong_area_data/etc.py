import pandas as pd


def preprocess(area_df: pd.DataFrame, crop: str) -> pd.DataFrame:
    area_df.columns = list(area_df.iloc[0, :])

    area_df = area_df.drop(index=0)

    area_df = area_df[["시도별", crop]]

    area_df.columns = ["시도별"] + [str(year) for year in range(2001, 2021)]

    # 결측값은 0 으로 설정
    area_df = area_df.fillna(0)

    # "-" 를 0으로 설정
    area_df = area_df.replace("-", 0)

    return area_df


if __name__ == "__main__":

    input_path = "../area_data/"
    output_path = "../preprocessed_area_data/"

    fruit_input_file = "유채참깨들깨땅콩_재배면적_2001_2020.csv"

    fruit_list = ['참깨', '땅콩']

    fruit_output_file_list = ["참깨_-_면적.csv", "땅콩_-_면적.csv"]

    df = pd.read_csv(input_path + fruit_input_file, encoding="euc-kr")

    for crop, output_file in zip(fruit_list, fruit_output_file_list):
        crop_area_df = preprocess(df, crop)

        crop_area_df.to_csv(output_path + output_file, index=False, encoding="utf-8-sig")

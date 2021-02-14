import pandas as pd


# return area, prod dataframe
def preprocess(fruit_df: pd.DataFrame, crop: str) -> (pd.DataFrame, pd.DataFrame):

    col_list = ["시도별"] + [str(year) for year in range(2001, 2021)]

    fruit_df.columns = list(fruit_df.iloc[0, :])

    fruit_df = fruit_df.drop(index=0)

    columns_List = pd.Series(fruit_df.columns)

    area_col_idx = [0] + [i for i, v in columns_List.items() if crop in v]
    prod_col_idx = [0] + [i + 2 for i in area_col_idx[1:]]

    crop_area_df = fruit_df.iloc[:, [idx for idx in area_col_idx]]
    crop_prod_df = fruit_df.iloc[:, [idx for idx in prod_col_idx]]

    crop_area_df.columns = col_list
    crop_prod_df.columns = col_list

    # 결측값은 0 으로 설정
    crop_area_df = crop_area_df.fillna(0)
    crop_prod_df = crop_prod_df.fillna(0)

    # "-" 를 0으로 설정
    crop_area_df = crop_area_df.replace("-", 0)
    crop_prod_df = crop_prod_df.replace("-", 0)

    return crop_area_df, crop_prod_df


if __name__ == "__main__":

    input_path = "../area_prod_data/"
    area_output_path = "../preprocessed_area_data/"
    prod_output_path = "../preprocessed_prod_data/"

    etc_input_file = "특용작물생산량_2001_2020.csv"

    etc_list = ["땅콩", "참깨"]

    etc_df = pd.read_csv(input_path + etc_input_file, encoding="euc-kr")

    for crop in etc_list:
        crop_area_df, crop_prod_df = preprocess(etc_df, crop)

        area_output_file = crop + "_-_면적.csv"
        prod_output_file = crop + "_-_생산량.csv"

        crop_area_df.to_csv(area_output_path + area_output_file, index=False, encoding="utf-8-sig")
        crop_prod_df.to_csv(prod_output_path + prod_output_file, index=False, encoding="utf-8-sig")

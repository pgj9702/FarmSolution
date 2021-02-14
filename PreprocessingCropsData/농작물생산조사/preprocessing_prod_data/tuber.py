import pandas as pd


# return area, prod dataframe
def preprocess(tuber_df: pd.DataFrame, crop: str, kind: str) -> (pd.DataFrame, pd.DataFrame):

    if kind == "-":
        kind = ""

    col_list = ["시도별"] + [str(year) for year in range(2001, 2021)]

    tuber_df.columns = list(tuber_df.iloc[0, :])

    tuber_df = tuber_df.drop(index=0)

    columns_List = pd.Series(tuber_df.columns)

    area_col_idx = [0] + [i for i, v in columns_List.items() if crop in v if kind in v]
    prod_col_idx = [0] + [i + 2 for i in area_col_idx[1:]]

    crop_area_df = tuber_df.iloc[:, [idx for idx in area_col_idx]]
    crop_prod_df = tuber_df.iloc[:, [idx for idx in prod_col_idx]]

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

    tuber_input_file = "서류생산량_생서_2001_2020.csv"

    tuber_list = ["감자_봄", "감자_가을", "감자_고랭지"]

    tuber_df = pd.read_csv(input_path + tuber_input_file, encoding="euc-kr")

    for tuber in tuber_list:

        crop = tuber.split("_")

        # 품종이 있으면 분류 (품목, 품종)
        if len(crop) == 2:
            crop, kind = crop

        elif len(crop) == 1:
            crop, kind = crop[0], ""

        area_output_file = crop + "_" + kind + "_면적.csv"
        prod_output_file = crop + "_" + kind + "_생산량.csv"

        fruit_area_df, fruit_prod_df = preprocess(tuber_df, crop, kind)

        fruit_area_df.to_csv(area_output_path + area_output_file, index=False, encoding="utf-8-sig")
        fruit_prod_df.to_csv(prod_output_path + prod_output_file, index=False, encoding="utf-8-sig")

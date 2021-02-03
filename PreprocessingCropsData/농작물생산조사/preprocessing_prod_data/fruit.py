import pandas as pd


def preprocess(area_df: pd.DataFrame, crop: str) -> pd.DataFrame:
    area_df.columns = list(area_df.iloc[0, :])

    area_df = area_df.drop(index=0)

    range_year = len(list(area_df[crop + "(성과수)"].columns))

    area_df = area_df[["시도별", crop + "(성과수)"]]

    area_df.columns = ["시도별"] + [str(2020 - i) for i in range(range_year - 1, -1, -1)]

    # 결측값은 0 으로 설정
    area_df = area_df.fillna(0)

    # "-" 를 0으로 설정
    area_df = area_df.replace("-", 0)

    return area_df


if __name__ == "__main__":

    input_path = "../production_data/"
    prod_output_path = "../preprocessed_prod_data/"
    area_output_path = "../preprocessed_area_data/"

    fruit_input_file = "과실생산량_2001_2020.csv"

    fruit_list = ['사과', '배', '복숭아', '포도', '감귤', '단감']

    prod_output_file_list = ["사과_-_생산량.csv", "배_-_생산량.csv", "복숭아_-_생산량.csv",
                              "포도_-_생산량.csv", "감귤_-_생산량.csv", "단감_-_생산량.csv"]

    area_output_file_list = ["사과_-_면적.csv", "배_-_면적.csv", "복숭아_-_면적.csv",
                              "포도_-_면적.csv", "감귤_-_면적.csv", "단감_-_면적.csv"]

    col_list = ["시도별"] + [str(year) for year in range(2001, 2021)]

    df = pd.read_csv(input_path + fruit_input_file, encoding="euc-kr")

    df.columns = list(df.iloc[0, :])

    df = df.drop(index=0)

    columns_List = pd.Series(df.columns)

    area_col_idx = [i for i, v in columns_List.items() if "사과" in v]
    prod_col_idx = [0] + [i+2 for i in area_col_idx]
    area_col_idx = [0] + area_col_idx

    crop_area_df = df.iloc[:, [idx for idx in area_col_idx]]
    crop_prod_df = df.iloc[:, [idx for idx in prod_col_idx]]

    crop_area_df.columns = col_list
    crop_prod_df.columns = col_list

    print(crop_prod_df)
    print(crop_area_df)

    crop_area_df.to_csv(area_output_path + area_output_file_list[0], index=False, encoding="utf-8-sig")
    crop_prod_df.to_csv(prod_output_path + prod_output_file_list[0], index=False, encoding="utf-8-sig")

    # print(df)

    # for i in list(df.iloc[0, :]):
    #     print(i)

    # for crop, output_file in zip(fruit_list, fruit_output_file_list):
    #     crop_area_df = preprocess(df, crop)
    #
    #     crop_area_df.to_csv(output_path + output_file, index=False, encoding="utf-8-sig")

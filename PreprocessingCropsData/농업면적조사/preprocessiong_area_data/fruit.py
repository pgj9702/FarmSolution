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

    input_path = "../area_data/"
    output_path = "../preprocessed_area_data/"

    fruit_input_file = "노지_과수_재배면적_2001_2020.csv"

    fruit_list = ['사과', '배', '복숭아', '포도', '감귤', '단감']

    fruit_output_file_list = ["사과_-_면적.csv", "배_-_면적.csv", "복숭아_-_면적.csv",
                              "포도_-_면적.csv", "감귤_-_면적.csv", "단감_-_면적.csv"]

    df = pd.read_csv(input_path + fruit_input_file, encoding="euc-kr")

    for crop, output_file in zip(fruit_list, fruit_output_file_list):
        crop_area_df = preprocess(df, crop)

        crop_area_df.to_csv(output_path + output_file, index=False, encoding="utf-8-sig")

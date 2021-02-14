import pandas as pd


def preprocess(v_type: str, vegetable_input_files: dict, vegetable_dict: dict) -> pd.DataFrame:
    vegetable_df = pd.read_csv(input_path + vegetable_input_files[v_type], encoding="euc-kr")

    vegetable_df.columns = list(vegetable_df.iloc[0, :])

    vegetable_df = vegetable_df.drop(index=0)

    columns_list = pd.Series(vegetable_df.columns)

    # 결측값은 0 으로 설정
    vegetable_df = vegetable_df.fillna(0)

    # "-" 를 0으로 설정
    vegetable_df = vegetable_df.replace("-", 0)

    # 원소들의 타입을 int 로 변환
    vegetable_df.iloc[:, 1:] = vegetable_df.iloc[:, 1:].apply(lambda x: pd.to_numeric(x))

    for vegetable in vegetable_dict[v_type]:

        crop = vegetable.split("_")

        # 품종이 있으면 분류 (품목, 품종)
        if len(crop) == 2:
            crop, kind = crop
            basic_col_name = kind + crop + ":면적 (ha)"
            area_col_idx = [i for i, v in columns_list.items() if crop in v if kind in v]

        elif len(crop) == 1:
            crop, kind = crop[0], "-"
            basic_col_name = crop + ":면적 (ha)"
            area_col_idx = [i for i, v in columns_list.items() if crop in v]

        col_idx_lists = pd.Series([[], [], []])
        area_output_file = crop + "_" + kind + "_면적.csv"
        prod_output_file = crop + "_" + kind + "_생산량.csv"

        for idx in area_col_idx:
            col_name = columns_list[idx]

            if col_name == basic_col_name:
                col_idx_lists[0].append(idx)

            elif "노지" in col_name:
                col_idx_lists[1].append(idx)

            elif "일반" in col_name:
                col_idx_lists[2].append(idx)

        for idx in range(len(col_idx_lists)):
            if len(col_idx_lists[idx]) == 0:
                del col_idx_lists[idx]
            else:
                range_year = len(col_idx_lists[idx])

        first_col_list = col_idx_lists[col_idx_lists.index[0]]
        crop_area_df = pd.DataFrame(vegetable_df.iloc[:, [0] + first_col_list])
        crop_prod_df = pd.DataFrame(vegetable_df.iloc[:, [0] + [i + 2 for i in first_col_list]])

        if len(col_idx_lists) > 1:

            for list_idx in col_idx_lists.index[1:]:
                sum_area_df = vegetable_df.iloc[:, col_idx_lists[list_idx]]
                sum_prod_df = vegetable_df.iloc[:, [i + 2 for i in col_idx_lists[list_idx]]]

                for col_idx in range(len(crop_area_df.columns) - 1):
                    crop_area_df.iloc[:, col_idx + 1] = crop_area_df.iloc[:, col_idx + 1] + sum_area_df.iloc[:, col_idx]
                    crop_prod_df.iloc[:, col_idx + 1] = crop_prod_df.iloc[:, col_idx + 1] + sum_prod_df.iloc[:, col_idx]

        crop_area_df.columns = ["시도별"] + [str(2020 - i) for i in range(range_year - 1, -1, -1)]
        crop_prod_df.columns = ["시도별"] + [str(2020 - i) for i in range(range_year - 1, -1, -1)]

        crop_area_df.to_csv(area_output_path + area_output_file, index=False, encoding="utf-8-sig")
        crop_prod_df.to_csv(prod_output_path + prod_output_file, index=False, encoding="utf-8-sig")


if __name__ == "__main__":

    input_path = "../area_prod_data/"
    area_output_path = "../preprocessed_area_data/"
    prod_output_path = "../preprocessed_prod_data/"

    vegetable_type = ["과채류", "근채류", "엽채류", "조미채소"]

    vegetable_input_files = {"과채류": "채소생산량_과채류_2001_2019.csv",
                             "근채류": "채소생산량_근채류_2001_2020.csv",
                             "엽채류": "채소생산량_엽채류_2001_2020.csv",
                             "조미채소": "채소생산량_조미채소_2001_2020.csv"}

    vegetable_dict = {"과채류": [], "근채류": ["무_봄", "무_가을", "무_겨울", "무_고랭지", "당근"],
                      "엽채류": ["배추_봄", "배추_가을", "배추_겨울", "배추_고랭지", "시금치", "양배추"],
                      "조미채소": ["고추", "대파", "마늘", "생강", "양파", "쪽파"]}

    for v_type in vegetable_type:
        preprocess(v_type, vegetable_input_files, vegetable_dict)

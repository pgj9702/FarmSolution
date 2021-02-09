import pandas as pd


def preprocess(vegetable_df: pd.DataFrame, crop: str) -> pd.DataFrame:
    col_name_list = ["시도별"] + [str(year) for year in range(2001, 2021)]

    vegetable_df.columns = list(vegetable_df.iloc[0, :])

    vegetable_df = vegetable_df.drop(index=0)

    columns_list = pd.Series(vegetable_df.columns)

    area_col_idx = [0] + [i for i, v in columns_list.items() if crop in v]
    prod_col_idx = [0] + [i + 2 for i in area_col_idx[1:]]

    crop_area_df = vegetable_df.iloc[:, [idx for idx in area_col_idx]]
    crop_prod_df = vegetable_df.iloc[:, [idx for idx in prod_col_idx]]

    crop_area_df.columns = col_name_list
    crop_prod_df.columns = col_name_list

    # 결측값은 0 으로 설정
    crop_area_df = crop_area_df.fillna(0)
    crop_prod_df = crop_prod_df.fillna(0)

    # "-" 를 0으로 설정
    crop_area_df = crop_area_df.replace("-", 0)
    crop_prod_df = crop_prod_df.replace("-", 0)

    return crop_area_df, crop_prod_df


if __name__ == "__main__":

    input_path = "../area_prod_data/"
    output_path = "../preprocessed_prod_data/"

    vegetable_type = ["과채류", "근채류", "엽채류", "조미채소"]

    vegetable_input_files = {"과채류": "채소생산량_과채류_2001_2019.csv",
                             "근채류": "채소생산량_근채류_2001_2020.csv",
                             "엽채류": "채소생산량_엽채류_2001_2020.csv",
                             "조미채소": "채소생산량_조미채소_2001_2020.csv"}

    vegetable_dict = {"과채류": [], "근채류": ["무_봄", "무_가을", "무_겨울", "무_고랭지", "당근"],
                      "엽채류": ["배추_봄", "배추_가을", "배추_겨울", "배추_고랭지", "시금치", "양배추"],
                      "조미채소": ["고추", "대파", "마늘", "생강", "양파", "쪽파"]}

    vegetable_output_file_list = ["무_봄_면적.csv", "무_고랭지_면적.csv", "무_가을_면적.csv", "무_겨울_면적.csv",
                                  "당근_-_면적.csv", "배추_봄_면적.csv", "배추_고랭지_면적.csv", "배추_가을_면적.csv",
                                  "배추_겨울_면적.csv", "시금치_-_면적.csv", "양배추_-_면적.csv", "고추_-_면적.csv",
                                  "마늘_-_면적.csv", "대파_-_면적.csv", "쪽파_-_면적.csv", "양파_-_면적.csv",
                                  "생강_-_면적.csv"]


    col_list = ["시도별"] + [str(year) for year in range(2001, 2021)]

    for v_type in vegetable_type:
        vegetable_df = pd.read_csv(input_path + vegetable_input_files[v_type], encoding="euc-kr")

        vegetable_df.columns = list(vegetable_df.iloc[0, :])

        vegetable_df = vegetable_df.drop(index=0)

        columns_list = pd.Series(vegetable_df.columns)

        for vegetable in vegetable_dict[v_type]:

            crop = vegetable.split("_")

            # 품종이 있으면 분류 (품목, 품종)
            if len(crop) == 2:
                crop, kind = crop
                basic_col_name = kind + crop + ":면적 (ha)"
                area_col_idx = [i for i, v in columns_list.items() if crop in v if kind in v]

            elif len(crop) == 1:
                crop = crop[0]
                basic_col_name = crop + ":면적 (ha)"
                area_col_idx = [i for i, v in columns_list.items() if crop in v]

            col_idx_lists = [[], [], []]

            basic_col_idx = []
            noji_col_idx = []
            normal_col_idx = []

            for idx in area_col_idx:
                col_name = columns_list[idx]

                if col_name == basic_col_name:
                    col_idx_lists[0].append(idx)

                elif "노지" in col_name:
                    col_idx_lists[1].append(idx)

                elif "일반" in col_name:
                    col_idx_lists[2].append(idx)

            # 기본, 노지, 일반 의 생산량, 면적 합산
            # print("basic", len(basic_col_idx))
            # print("noji", len(noji_col_idx))
            # print("normal", len(normal_col_idx))

            for idx in range(len(col_idx_lists)):
                if len(col_idx_lists[idx]) == 0:
                    col_idx_lists.remove(idx)

            print(col_idx_lists)


            # print(vegetable_df.iloc[:, []])

            crop_area_df = pd.DataFrame()
            crop_prod_df = pd.DataFrame()






            # crop, kind = crop
            # area_col_idx = [0] + [i for i, v in columns_list.items() if crop in v if kind in v]
            #
            # crop = crop[0]
            # area_col_idx = [0] + [i for i, v in columns_list.items() if crop in v]

            # prod_col_idx = [0] + [i + 2 for i in area_col_idx[1:]]
            #
            # crop_area_df = vegetable_df.iloc[:, [idx for idx in area_col_idx]]
            # crop_prod_df = vegetable_df.iloc[:, [idx for idx in prod_col_idx]]
            #
            # # 일반과 노지를 합산
            # asd = crop_area_df.columns[1:].str.split(":")
            #
            # print(crop_area_df.columns[1:])


    # crop_area_df.columns = col_list
    # crop_prod_df.columns = col_list
    #
    # # np.prod([,], axis=0)
    #
    # # 결측값은 0 으로 설정
    # crop_area_df = crop_area_df.fillna(0)
    # crop_prod_df = crop_prod_df.fillna(0)
    #
    # # "-" 를 0으로 설정
    # crop_area_df = crop_area_df.replace("-", 0)
    # crop_prod_df = crop_prod_df.replace("-", 0)

    # len_moo = [x for x in list(df.loc[0, :]) if "당근" in x]
    # print(len(len_moo))

    # for crop, output_file in zip(vegetable_dict["근채류"], vegetable_output_file_list):
    #     crop_area_df = preprocess(df, crop)
    #
    #     crop_area_df.to_csv(output_path + output_file, index=False, encoding="utf-8-sig")

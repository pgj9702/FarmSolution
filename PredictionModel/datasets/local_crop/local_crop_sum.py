import os
import pandas as pd


def local_crop_kind(location_df: pd.DataFrame) -> (pd.DataFrame):
    location = location_df


if __name__ == '__main__':
    input_path = '../../../PreprocessingCropsData/농작물생산조사/preprocessed_prod_data/'

    location_input_file = '배추_가을_생산량.csv'
    location_df = pd.read_csv(input_path + location_input_file)
    location = local_crop_kind(location_df)

    file_list = os.listdir(input_path)

    crop_list = [crop.split("_")[0] + "_" + crop.split("_")[1] for crop in file_list]

    # print(file_list)

    # 작물 list 만들기
    crop_data_df = []

    for file_name, crop_name in zip(file_list, crop_list):
        temp_df = pd.read_csv(input_path + file_name)
        temp_df = temp_df.drop(temp_df.index[0])
        # print(temp_df)

        temp_df["작물"] = crop_name
        crop_data_df.append(temp_df)

    crop_data_df = pd.concat(crop_data_df, ignore_index=True)

    # 작물 Data [1]에 배치
    crop_data_df_crop_col = crop_data_df["작물"]

    crop_data_df.drop("작물", axis=1, inplace=True)

    crop_data_df.insert(1, "작물", crop_data_df_crop_col)
    # print(crop_data_df)

    # 모든 row가 0인 지역 제거
    not_null_row_index = (crop_data_df.iloc[:, 2:] == 0).all(axis='columns')

    not_null_row_index = not_null_row_index[not_null_row_index].index

    crop_data_df.drop(not_null_row_index, inplace=True)
    crop_data_df = crop_data_df.fillna(0)
    # crop_data_df = crop_data_df.dropna(axis=1)

    # index 초기화
    crop_data_df.reset_index(drop=True, inplace=True)
    crop_data_df = crop_data_df.set_index('시도별')
    crop_data_df = pd.DataFrame(crop_data_df)
    # print(crop_data_df.index)

    print(crop_data_df.head(15))

    # 년도별로 작물 list
    crop_data_df = crop_data_df.groupby('시도별').agg(lambda x: x.tolist())
    # print(crop_data_df.iloc[:, :2])

crop_data_df.to_csv('local_crop.csv', encoding="utf-8-sig")
print(crop_data_df)
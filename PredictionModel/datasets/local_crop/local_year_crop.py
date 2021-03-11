import pandas as pd

def loc_crop(location_df:pd.DataFrame) -> (pd.DataFrame):
  location = location_df
  location = location.set_index("년도")
  location = location.drop(location.columns[2:], axis=1)
  print(location)

  spe_loc = location.iloc[:4, :]
  print(spe_loc)

import os
import pandas as pd

if __name__ == "__main__":

  input_path = "/content/FarmSolution/PredictionModel/datasets/default/"
  location_input_file = "배추_가을_dataset.csv"
  location_df = pd.read_csv(input_path + location_input_file)
  location = loc_crop(location_df)

  file_list = os.listdir(input_path)

  crop_list = [crop.split("_")[0] + "_" + crop.split("_")[1] for crop in file_list]

  print(file_list)

  local_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
       '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도',
       '제주도']

  # 최종 df
  crop_list_by_local = pd.DataFrame(columns=[year for year in range(2001, 2020)], index=local_list)

  print

  # 모든 작물 datasets 통합
  crop_data_df = []

  for file_name, crop_name in zip(file_list, crop_list):
    temp_df = pd.read_csv(input_path + file_name)
    temp_df = temp_df.loc[:, ["지역 이름", "년도"]]
    temp_df["작물"] = crop_name
    crop_data_df.append(temp_df)

  crop_data_df = pd.concat(crop_data_df, ignore_index=True)

  for year in range(2001, 2020):
    temp_df = crop_data_df[crop_data_df["년도"] == year]

    for local in local_list:
      crop_by_local_year = temp_df[temp_df["지역 이름"] == local]["작물"]
      crop_list_by_local.loc[local, year] = list(crop_by_local_year)

  crop_list_by_local.to_csv("test.csv", encoding="utf-8-sig")

  print(crop_list_by_local)

import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

def scaling_dataset(scaling="default"):
    print(scaling)

    dir_path = "../datasets/종관기상관측/default/"

    file_list = os.listdir(dir_path)

    scaling_list = ["standard", "robust", "minmax"]

    path_to_save = "../datasets/종관기상관측/"

    if scaling == "standard":
        scaler = StandardScaler()
        path_to_save = path_to_save + "standard/"

    elif scaling == "robust":
        scaler = RobustScaler()
        path_to_save = path_to_save + "robust/"

    elif scaling == "minmax":
        scaler = MinMaxScaler()
        path_to_save = path_to_save + "minmax/"

    else:
        return 0

    try:
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)
    except OSError:
        print('Error: Creating directory. ' + path_to_save)

    for file in file_list:

        dataset_df = pd.read_csv(dir_path + file)

        temp_df = dataset_df.drop(["지역", "년도"], axis=1)

        dataset_df = dataset_df.loc[:, ["지역", "년도"]]

        transform_df_columns = temp_df.columns

        scaler.fit(temp_df)

        transform_df = pd.DataFrame(scaler.transform(temp_df), columns=transform_df_columns)

        dataset_df = pd.concat([dataset_df, transform_df], axis=1)

        file_name = file.split("d", maxsplit=1)[0]

        print(file_name)

        # print(dataset_df)

        dataset_df.to_csv(path_to_save + file_name + scaling + "_dataset.csv", encoding="utf-8-sig")


if __name__ == "__main__":
    # path_to_save =

    scaler_list = ["minmax", "robust", "standard"]

    for scaler in scaler_list:
        scaling_dataset(scaling=scaler)




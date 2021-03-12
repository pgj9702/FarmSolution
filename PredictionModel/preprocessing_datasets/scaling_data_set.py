import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

def scaling_dataset(scaler="default"):

    dir_path = "../datasets/종관기상관측/default/"

    file_list = os.listdir(dir_path)

    for file in file_list:

        dataset_df = pd.read_csv(dir_path + file)

        temp_df = dataset_df.drop(["지역", "년도"], axis=1)

        dataset_df = dataset_df.loc[:, ["지역", "년도"]]

        transform_df_columns = temp_df.columns

        if scaler == "standard":
            scaler = StandardScaler()

        elif scaler == "robust":
            scaler = RobustScaler()

        elif scaler == "minmax":
            scaler = MinMaxScaler()

        else: return 0

        scaler.fit(temp_df)

        transform_df = pd.DataFrame(scaler.transform(temp_df), columns=transform_df_columns)

        dataset_df = pd.concat([dataset_df, transform_df], axis=1)

        print(dataset_df)




if __name__ == "__main__":
    # path_to_save =

    scaler_list = ["minmax", "robust", "standard"]

    for scaler in scaler_list:
        scaling_dataset(scaler=scaler)




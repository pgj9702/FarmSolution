import numpy as np
import pandas as pd
import os
import datetime as dt
from sklearn.preprocessing import MinMaxScaler


# 데이터 분할을 위한 함수
def get_train_test_datasets(path, crop_kind, start_ymd, end_ymd, minmaxscaler=True):

    train_set = pd.read_csv(path + crop_kind + "_dataset.csv")

    train_set = train_set.set_index('년도')

    train_set = train_set.drop("지역 이름", axis=1)

    # print(train_set)

    if minmaxscaler:

        train_set_columns = train_set.columns

        train_set_indexes = list(train_set.index.values)

        min_max_scaler = MinMaxScaler()

        min_max_scaler.fit(train_set)

        train_set = min_max_scaler.transform(train_set)

        train_set = pd.DataFrame(train_set, columns=train_set_columns, index=train_set_indexes)

    target = train_set["생산량"]

    train_set = train_set.drop("생산량", axis=1)

    X_train, X_test = train_set.loc[start_ymd:end_ymd, :], train_set.loc[end_ymd + 1:, :]

    y_train, y_test = target.loc[start_ymd:end_ymd], target.loc[end_ymd + 1:]

    return X_train, X_test, y_train, y_test, min_max_scaler


if __name__ == "__main__":
    path = ""
    X_train, X_test, y_train, y_test, min_max_scaler = get_train_test_datasets(path, "복숭아_-", 2010, 2018)

    print(X_train)
    print(y_train)
    print(X_test)
    print(y_test)

    # datasets_files = [csv for csv in os.listdir() if ".csv" in csv]
    #
    # print(datasets_files)
    #
    # max_len = 0
    #
    # for file in datasets_files:
    #     df = pd.read_csv(file)
    #
    #     df_len = len(df)
    #
    #     print(file, df_len)
    #
    #     if max_len < df_len:
    #         max_len = df_len
    #         max_data_file = file
    #
    #
    # print("데이터가 가장 많은 csv", max_data_file, max_len)





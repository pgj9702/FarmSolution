import pandas as pd
import os, sys
import matplotlib.pyplot as plt
import numpy as np

# ML model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.svm import LinearSVR
from sklearn.linear_model import SGDRegressor
from sklearn.svm import SVR

# 결측치 처리 KNN Imputer
from sklearn.impute import KNNImputer

# 최적 파라미터터
from sklearn.model_selection import GridSearchCV

# scaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler

import params_grids

def find_best_model(dataset: pd.DataFrame) -> dict:
    linear_model = LinearRegression()
    ridge_model = Ridge()
    lasso_model = Lasso()
    elasticNet_model = ElasticNet()
    linear_svr_model = LinearSVR()
    sgd_model = SGDRegressor()
    svr_model = SVR()

    ml_dict = {
        "linear": linear_model,
        "ridge": ridge_model,
        "lasso": lasso_model,
        "elasticNet": elasticNet_model,
        "linear_svr": linear_svr_model,
        "sgd": sgd_model,
        "svr": svr_model
    }

    scaler_dict = {"minmax": MinMaxScaler(), "robust": RobustScaler(), "standard": StandardScaler()}

    PARAMS_GRIDS = params_grids.PARAMS_GRIDS

    best_model_info = dict()

    best_model_info2 = dict()

    best_score = 0

    best_score2 = 0

    grid_search_flag = False

    # 데이터 세트 dict (생산량, 생산량(특성제거), 면적당생산량, 면적당생산량(특성제거))
    # 1: prod_dataset, 2: prod_per_area_dataset, 3: prod_dataset_corr, 4: prod_per_area_dataset_corr
    dataset_dict = dict()

    # KNN 으로 결측치 채우기
    imputer = KNNImputer()

    dataset.drop("지역", axis=1, inplace=True)

    dataset_filled = imputer.fit_transform(dataset)

    dataset = pd.DataFrame(dataset_filled, columns=dataset.columns)

    # 년도 col
    year_series = dataset["년도"]

    # 생산량 타겟
    prod_dataset = dataset.drop(["년도"], axis=1)
    prod_dataset.rename(columns={"생산량": "target"}, inplace=True)
    prod_dataset["년도"] = year_series
    dataset_dict[1] = prod_dataset

    prod_dataset_corr = prod_dataset.copy()    # 특성 제거될 dataset

    # 면적당 생산량 타겟
    prod_per_area_dataset = dataset
    prod_per_area_dataset["생산량"] = prod_per_area_dataset["생산량"] / prod_per_area_dataset["면적"]
    prod_per_area_dataset.drop(["면적", "년도"], axis=1, inplace=True)
    prod_per_area_dataset["년도"] = year_series
    prod_per_area_dataset.rename(columns={"생산량": "target"}, inplace=True)
    dataset_dict[2] = prod_per_area_dataset

    prod_per_area_dataset_corr = prod_per_area_dataset.copy()  # 특성 제거될 dataset
    
    # 특성 제거 : 상관계수 0.2이하 제거 / 제거 없이
    # 생산량
    corr_matrix = prod_dataset.corr()

    prod_corr_result = corr_matrix["target"]

    for feature, corr in prod_corr_result.items():
        if abs(corr) < 0.2:
            prod_dataset_corr.drop(feature, axis=1, inplace=True)

    # 특성 개수가 너무 적으면 제외함
    if len(prod_dataset_corr.columns) > 7:
        prod_dataset_corr["년도"] = year_series
        dataset_dict[3] = prod_dataset_corr

    # 면적당 생산량
    corr_matrix = prod_per_area_dataset.corr()

    prod_per_area_corr_result = corr_matrix["target"]

    for feature, corr in prod_per_area_corr_result.items():
        if abs(corr) < 0.2:
            prod_per_area_dataset_corr.drop(feature, axis=1, inplace=True)

    # 특성 개수가 너무 적으면 제외함
    if len(prod_per_area_dataset_corr.columns) > 7:
        prod_per_area_dataset_corr["년도"] = year_series
        dataset_dict[4] = prod_per_area_dataset_corr

    # 1: prod_dataset, 2: prod_per_area_dataset, 3: prod_dataset_corr, 4: prod_per_area_dataset_corr
    # 기간 : 최근 5개 데이터 셋에 대하여 각각 학습해서 예측한 결과를 rmse
    # 기간은 3~10년, target year 는 2015~2019
    range_year_list = [range_year for range_year in range(3, 11)]
    target_year = 2019

    # 알고리즘
    # 데이터세트
    for dataset_num, learning_data in dataset_dict.items():

        for str_Ml, ML in ml_dict.items():
            print(str_Ml, "dataset", dataset_num, "testing...")
            if str_Ml in PARAMS_GRIDS.keys():
                # 최적 파라미터
                # 사이킷런의 GridSearchCV -> GridSearch + Cross Validation을 동시에 지원
                # 파라미터 dict 설정
                params_grid = PARAMS_GRIDS[str_Ml]
                # params_grid = [
                #     {"fit_intercept": [False, True]}
                # ]
                # neg_mean_squared_error, neg_root_mean_squared_error, r2
                grid_search = GridSearchCV(ML, params_grid, cv=3, n_jobs=-1, scoring="r2")

                grid_search_flag = True

            # 기간에 맞게 데이터 세트 만들기
            for range_year in range_year_list:

                # scaler
                # scaler 적용, 데이터프레임으로 다시 변환
                start_year = target_year - range_year

                for scaler_name, scaler in scaler_dict.items():
                    copy_dataset = learning_data.copy()

                    train_dataset_index = copy_dataset[(copy_dataset["년도"] >= start_year) &
                                                  (copy_dataset["년도"] < target_year)
                                                  ].index

                    test_dataset_index = copy_dataset[copy_dataset["년도"] == target_year].index

                    copy_dataset.drop("년도", axis=1, inplace=True)
                    scaler.fit(copy_dataset)

                    train_dataset = scaler.transform(copy_dataset.iloc[train_dataset_index])
                    test_dataset = scaler.transform(copy_dataset.iloc[test_dataset_index])

                    X_train = train_dataset[:, 1:]
                    X_test = test_dataset[:, 1:]
                    y_train = train_dataset[:, 0]
                    y_test = test_dataset[:, 0]

                    if grid_search_flag == True:
                        grid_search.fit(X_train, y_train)
                        score = grid_search.score(X_test, y_test)
                        best_params = grid_search.best_params_
                        # print("dataset num:", dataset_num, "\talgorithm :", str_Ml, "\t년도 설정 :", start_year, "\tscaler :", scaler_name)
                        # print("params", best_params)
                        # print("score", score)

                        if best_score < score:
                            best_score = score
                            best_model_info["dataset"] = dataset_num
                            best_model_info["algorithm"] = str_Ml
                            best_model_info["start_year"] = start_year
                            best_model_info["scaler"] = scaler_name
                            best_model_info["params"] = best_params
                            best_model_info["score"] = score

                    else:
                        ML.fit(X_train, y_train)
                        score = ML.score(X_test, y_test)
                        # print("dataset num:", dataset_num, "\talgorithm :", str_Ml, "\t년도 설정 :", start_year, "\tscaler :", scaler_name)
                        # print("score", ML.score(X_test, y_test))

                        if best_score < score:
                            best_score = score
                            best_model_info["dataset"] = dataset_num
                            best_model_info["algorithm"] = str_Ml
                            best_model_info["start_year"] = start_year
                            best_model_info["scaler"] = scaler_name
                            best_model_info["params"] = best_params
                            best_model_info["score"] = score

            grid_search_flag = False

    # 가장 좋은 알고리즘과 최적 파라미터
    print("test", best_model_info)

    return best_model_info


if __name__ == "__main__":

    file_path = "./datasets/종관기상관측/default/"

    file_list = os.listdir(file_path)

    best_model_df = pd.DataFrame(
        columns=["crop", "algorithm", "dataset", "start_year", "scaler", "params", "score", "segmentation"])

    print(file_list)

    dataset_file_list = []
    seg_dataset_file_list = []

    for file in file_list:
        if "seg" in file:
            seg_dataset_file_list.append(file)
        else:
            dataset_file_list.append(file)

    for seg_dataset_file, dataset_file in zip(seg_dataset_file_list, dataset_file_list):
        crop_name = dataset_file.split("_d")[0]

        print(crop_name)

        # 데이터가 너무 없어서 실행 불가
        if "무_겨울" in crop_name:
            continue

        seg_dataset_df = pd.read_csv(file_path + seg_dataset_file)
        dataset_df = pd.read_csv(file_path + dataset_file)

        result_seg = find_best_model(seg_dataset_df)
        result_default = find_best_model(dataset_df)

        if result_seg["score"] > result_default["score"]:
            row_data = result_seg
            row_data["segmentation"] = "True"

        else:
            row_data = result_default
            row_data["segmentation"] = "False"

        row_data["crop"] = crop_name

        best_model_df = best_model_df.append(row_data, ignore_index=True)

    best_model_df.to_csv("crops_best_model.csv", index=False, encoding="utf-8-sig")
    best_model_df.to_excel("crops_best_model.xlsx", index=False, encoding="utf-8-sig")


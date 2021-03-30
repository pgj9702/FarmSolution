from django.apps import AppConfig
from . import models
from .predictive_modeling import predictive_modeling
import pandas as pd
from . import models_setting
from sklearn.impute import KNNImputer
import numpy as np

# ML model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.svm import LinearSVR
from sklearn.linear_model import SGDRegressor
from sklearn.svm import SVR

from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

class CropsConfig(AppConfig):
    name = 'crops'

    # 작물별 모델 생성
    models_by_crop = models_setting.MODELS_BY_CROP

    crop_list = [
        "감귤_-", "감자_가을", "감자_고랭지", "감자_봄", "고추_-", "단감_-", "당근_-",
        "대파_-", "땅콩_-", "마늘_-", "무_가을", "무_고랭지", "무_봄", "배_-", "배추_가을",
        "배추_겨울", "배추_고랭지", "배추_봄", "복숭아_-", "사과_-", "생강_-", "시금치_-",
        "양배추_-", "양파_-", "쪽파_-", "참깨_-", "포도_-"
    ]

    predict_prod = dict()
    predict_prod_per_area = dict()

    for crop, table_name, ml_model in zip(crop_list, models_by_crop.keys(), models_by_crop.values()):

        model_name = ml_model["model"]

        if model_name == "linear":
            ml = LinearRegression()
        elif model_name == "ridge":
            ml = Ridge(**ml_model["params"])
        elif model_name == "lasso":
            ml = Lasso(**ml_model["params"])
        elif model_name == "elasticNet":
            ml = ElasticNet(**ml_model["params"])
        elif model_name == "linear_svr":
            ml = LinearSVR(**ml_model["params"])
        elif model_name == "svr":
            ml = SVR(**ml_model["params"])
        elif model_name == "sgd":
            ml = SGDRegressor(**ml_model["params"])

        # 학습데이터 년도, 특성 제거, scaler, target
        dataset = pd.DataFrame(list(getattr(models, table_name).objects.all().values()))

        imputer = KNNImputer()

        dataset.drop("region", axis=1, inplace=True)

        dataset_filled = imputer.fit_transform(dataset)

        dataset = pd.DataFrame(dataset_filled, columns=dataset.columns)

        # 년도
        dataset = dataset[dataset["year"] >= ml_model["year"]]

        dataset.drop(["idx", "year"], axis=1, inplace=True)

        if ml_model["target"] != "prod":
            dataset["prod"] = dataset["prod"] / dataset["area"]
            dataset.drop("area", axis=1, inplace=True)

        del_feature_list = []

        # 특성 제거
        if ml_model["corr"]:
            corr_matrix = dataset.corr()

            prod_corr_result = corr_matrix["prod"]

            for feature, corr in prod_corr_result.items():
                if abs(corr) < 0.2:
                    dataset.drop(feature, axis=1, inplace=True)
                    del_feature_list.append(feature)

        if ml_model["scaler"] == "minmax":
            scaler = MinMaxScaler().fit(dataset)

        elif ml_model["scaler"] == "standard":
            scaler = RobustScaler().fit(dataset)

        elif ml_model["scaler"] == "robust":
            scaler = StandardScaler().fit(dataset)

        dataset_scaled = scaler.transform(dataset)

        ml.fit(dataset_scaled[:, 1:], dataset_scaled[:, 0])

        # 예측
        if ml_model["seg"]:
            predict_df = pd.DataFrame(list(getattr(models, "SegDataPredict").objects.all().values()))

        else:
            predict_df = pd.DataFrame(list(getattr(models, "DataPredict").objects.all().values()))


        predict_df = predict_df[predict_df["crop"] == crop]

        local_list = predict_df["region"].unique()

        crops_prod = dict()
        crops_prod_per_area = dict()
        for local in local_list:
            temp_df = predict_df[predict_df["region"] == local].copy()

            if ml_model["target"] != "prod":
                temp_df.drop("area", axis=1, inplace=True)

            temp_df.drop(["region", "crop"] + del_feature_list, axis=1, inplace=True)

            temp_df_scaled = scaler.transform(temp_df)

            temp_df_scaled = np.reshape(temp_df_scaled[0, 1:], (1, -1))

            result = list(ml.predict(temp_df_scaled))

            inverse_data = result + list(temp_df_scaled.flatten())

            # print("test")
            # print(result)
            # print(inverse_data)

            result = list(scaler.inverse_transform(np.reshape(inverse_data, (1, -1))).flatten())

            crops_prod[local] = result[0]
            crops_prod_per_area[local] = result[0] / result[1]

        predict_prod[crop] = crops_prod
        predict_prod_per_area[crop] = crops_prod_per_area

    print(predict_prod)
    print(predict_prod_per_area)


    #
    # for table in table_list:
    #     datasets_dict = dict()
    #
    #     dataset_df = pd.DataFrame(list(getattr(models, table).objects.all().values()))
    #
    #     datasets_dict[table] = dataset_df
    #
    # # predictive_models, key: 테이블명(작물명), value: 훈련된 모델 객체
    # predictive_models = predictive_modeling(datasets_dict)


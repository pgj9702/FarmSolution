from threading import local

import pandas as pd
import os, sys

from FarmSolution.PredictionModel.deep_learning.lstm import lstm
from FarmSolution.PredictionModel.deep_learning.rnn import rnn
from FarmSolution.PredictionModel.machine_learning.DecisionTree import decision_tree
from FarmSolution.PredictionModel.machine_learning.elasticnet import elastic_net
from FarmSolution.PredictionModel.machine_learning.extratreesclassifier import extratreeclassifier
from FarmSolution.PredictionModel.machine_learning.gradientboostingregressor import gradientboostingclassifier
from FarmSolution.PredictionModel.machine_learning.Lasso import lasso
from FarmSolution.PredictionModel.machine_learning.LinearRegression import reg
from FarmSolution.PredictionModel.machine_learning.linearsvr import linear_svr
from FarmSolution.PredictionModel.machine_learning.RandomForestRegressor import random_forest
from FarmSolution.PredictionModel.machine_learning.Ridge import ridge
from FarmSolution.PredictionModel.machine_learning.sgdregressor import sgdregressor
from FarmSolution.PredictionModel.machine_learning.svr import svr

from FarmSolution.PredictionModel.datasets.get_datasets import get_train_test_datasets
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt
import numpy as np

#한글 폰트 사용
from matplotlib import font_manager,rc
import matplotlib
import matplotlib.pyplot as plt

# 예측 모델의 score 를 그래프로 나타내어 파일로 저장
def score_graph(models: dict, X_test, y_test, min_max_scaler):

    df = pd.DataFrame(index=models.keys(), columns=["score"])

    for model_name, model in models.items():

        prediction = model.predict(X_test)

        real = np.concatenate((X_test, y_test), axis=None).reshape(1, -1)

        result = np.concatenate((X_test, prediction), axis=None).reshape(1, -1)

        y_real = min_max_scaler.inverse_transform(real).flatten()[9]

        y_prediction = min_max_scaler.inverse_transform(result).flatten()[9]

        # model_score = np.abs(y_test - prediction) / y_test * 100

        model_score = np.abs(y_real - y_prediction) / y_real * 100

        print(model_name, model_score, 100 - model_score)

        # model_score = model.score(X_test, y_test)

        df.loc[model_name, "score"] = 100 - model_score

    return df


# lstm, rnn, DecisionTree, elasticnet, extratreesclassifier.py, gradientboostingregressor.py, Lasso, LinearRegression
# linearsvr, RandomForestRegressor, Ridge, sgdregressor, svr

if __name__ == "__main__":

    crop_list = ['감귤_-', '감자_가을', '감자_고랭지', '단감_-', '배추_고랭지', '복숭아_-', '사과_-', '쪽파_-', '포도_-']

    df_list = []

    for crop in crop_list:

        path = "../datasets/"

        X_train, X_test, y_train, y_test, min_max_scaler = get_train_test_datasets(path, crop, 2010, 2018)

        # print(type(X_test.iloc[0]), type(y_test.iloc[0]))
        # print(list(X_test.iloc[0]))

        X_test = list(X_test.iloc[0])
        y_test = [y_test.iloc[0]]

        X_test = np.array(X_test).reshape(1, -1)
        y_test = np.array(y_test).reshape(1, -1)

        # print(X_test.shape, y_test.shape)

        # X_train = X_train.to_numpy()
        # X_test = X_test.to_numpy()
        # y_train = y_train.to_numpy()
        # y_test = y_test.to_numpy()
        #
        # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape, type(X_train), type(X_test), type(y_train), type(y_test))
        #
        # print(X_test)
        #
        # print(y_test)

        # X_test, y_test = X_test.iloc[0], y_test.iloc[0]

        # print( X_train, X_test, y_train, y_test)
        #
        # X_train = X_train.values
        # X_test = X_test.values
        # y_train = y_train.values
        # y_test = y_test.values
        #
        # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

        # lstm_model = lstm(X_train, y_train)
        # rnn_model= rnn(X_train, y_train)
        # decision_tree_model = decision_tree(X_train, y_train)
        elastic_net_model = elastic_net(X_train, y_train)
        # extratreeclassifier_model = extratreeclassifier(X_train, y_train)
        # gradientboostingclassifier_model = gradientboostingclassifier(X_train, y_train)
        lasso_model = lasso(X_train, y_train)
        reg_model = reg(X_train, y_train)
        linear_svr_model = linear_svr(X_train, y_train)
        # random_forest_model = random_forest(X_train, y_train)
        ridge_model = ridge(X_train, y_train)
        sgdregressor_model = sgdregressor(X_train, y_train)
        svr_model = svr(X_train, y_train)


        models = {
            # "lstm": lstm_model,
            # "rnn": rnn_model,
            # "decision_tree": decision_tree_model,
            "elasticnet": elastic_net_model,
            # "extratreeclassifier": extratreeclassifier_model,
            # "gradientboostingclassifier": gradientboostingclassifier_model,
            "lasso": lasso_model,
            "reg": reg_model,
            "linear_svr": linear_svr_model,
            # "random_forest": random_forest_model,
            "ridge": ridge_model,
            "sgdregressor": sgdregressor_model,
            "svr": svr_model
        }

        print(crop)

        df_list.append(score_graph(models, X_test, y_test, min_max_scaler))

    graph_df = pd.concat([df for df in df_list], axis=1)

    col_list = ['감귤', '감자_가을', '감자_고랭지', '단감', '배추_고랭지', '복숭아', '사과', '쪽파', '포도']

    graph_df.columns = col_list

    graph_df.reset_index(drop=False, inplace=True, col_fill="model")

    graph_df.rename(columns={"index": "model"}, inplace=True)

    print(graph_df)

    # 폰트 경로
    font_path = "C:/Windows/Fonts/H2GTRM.TTF"
    # 폰트 이름 얻어오기
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    # font 설정
    plt.rc('font', family=font_name)

    graph_df.plot(x="model", y=graph_df.columns[1:], kind="bar")

    plt.ylim([40, 110])
    plt.yticks(range(40, 110, 20))
    plt.legend(loc="upper center", ncol=9)
    plt.ylabel("score")
    plt.xticks(rotation='45')

    plt.show()


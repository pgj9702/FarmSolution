import pandas as pd
import os, sys

from FarmSolution.PredictionModel.deep_learning.lstm import lstm
from FarmSolution.PredictionModel.deep_learning.rnn import rnn
from FarmSolution.PredictionModel.machine_learning.DecisionTree import decision_tree
from FarmSolution.PredictionModel.machine_learning.elasticnet import elasticnet
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

import matplotlib.pyplot as plt


# 예측 모델의 score 를 그래프로 나타내어 파일로 저장
def score_graph(models: dict, y_train, y_test):

    df = pd.DataFrame(index=models.keys(), columns=["score"])

    print(df)

    for model_name, model in models.items():
        print("training", model_name)

        df.loc[model_name, "score"] = model.score(y_train, y_test)

    print(df)




# lstm, rnn, DecisionTree, elasticnet, extratreesclassifier.py, gradientboostingregressor.py, Lasso, LinearRegression
# linearsvr, RandomForestRegressor, Ridge, sgdregressor, svr

if __name__ == "__main__":

    path = "../datasets/"

    X_train, X_test, y_train, y_test = get_train_test_datasets(path, "배추_가을", 2010, 2018)

    # lstm = lstm(X_train, y_train)
    # rnn = rnn(X_train, y_train)
    # decision_tree = decision_tree(X_train, y_train)
    elasticnet = elasticnet(X_train, y_train)
    # extratreeclassifier = extratreeclassifier(X_train, y_train)
    # gradientboostingclassifier = gradientboostingclassifier(X_train, y_train)
    lasso = lasso(X_train, y_train)
    reg = reg(X_train, y_train)
    linear_svr = linear_svr(X_train, y_train)
    # random_forest = random_forest(X_train, y_train)
    ridge = ridge(X_train, y_train)
    sgdregressor = sgdregressor(X_train, y_train)
    svr = svr(X_train, y_train)


    models = {
        # "lstm": lstm,
        # "rnn": rnn,
        # "decision_tree": decision_tree,
        # "elasticnet": elasticnet,
        # "extratreeclassifier": extratreeclassifier,
        # "gradientboostingclassifier": gradientboostingclassifier,
        "lasso": lasso,
        "reg": reg,
        "linear_svr": linear_svr,
        # "random_forest": random_forest,
        "ridge": ridge,
        "sgdregressor": sgdregressor,
        "svr": svr
    }

    score_graph(models, y_train, y_test)


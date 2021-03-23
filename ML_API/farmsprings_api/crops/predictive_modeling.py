import models   # 작물 모델 import
from django.core.management.base import BaseCommand
import pymysql
import pandas as pd
from sklearn.linear_model import LinearRegression
import sklearn.linear_model
from django.conf import settings
import os
from . import models_setting
import sys
import pickle

# datasets_dict, key: 테이블명(작물명), value: DataFrame
# return predictive_models # key: 테이블명(작물명), value: 훈련된 모델 객체
def predictive_modeling(datasets_dict: dict) -> dict:

    models_by_crop = models_setting.MODELS_BY_CROP

    predictive_models = dict()

    # DB 로부터 테이블 목록(작물별 데이터셋) 을 가져옴

    # 문자열로 함수 호출 getattr(개체명, 함수의 이름(string))
    # getattr()

    for crop, dataset in datasets_dict.items():

        predictive_models[crop] = sklearn.linear_model.__dict__[models_by_crop[crop]["model"]](**models_by_crop[crop]["params"])
        print(sys.getsizeof(pickle.dumps(predictive_models[crop])))


    return predictive_models
    # elasticnet lasso reg linear_svr ridge sgdregressor svr



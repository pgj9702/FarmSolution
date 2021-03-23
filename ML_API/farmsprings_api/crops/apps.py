from django.apps import AppConfig
from . import models
from .predictive_modeling import predictive_modeling
import pandas as pd


class CropsConfig(AppConfig):
    name = 'crops'

    # 작물별 모델 생성
    table_list = dir(models)
    for not_table_name in ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
                           '__name__', '__package__', '__spec__', 'models']:
        table_list.remove(not_table_name)

    #
    for table in table_list:
        datasets_dict = dict()

        dataset_df = pd.DataFrame(list(getattr(models, table).objects.all().values()))

        datasets_dict[table] = dataset_df

    # predictive_models, key: 테이블명(작물명), value: 훈련된 모델 객체
    predictive_models = predictive_modeling(datasets_dict)


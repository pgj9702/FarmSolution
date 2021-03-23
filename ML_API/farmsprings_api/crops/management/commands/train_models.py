import pickle

from django.core.management.base import BaseCommand
import pymysql
import pandas as pd
from sklearn.linear_model import LinearRegression
from django.conf import settings
import os

class Command(BaseCommand):
    help = '실행 시 작물별 예측 모델을 학습'

    def handle(self, *args, **kwargs):
        # MySQL Connection 연결
        admin_conn = pymysql.connect(
            user='admin',
            password='bit1234',
            host='127.0.0.1',
            db='cropsdb',
            charset='utf8'
        )

        # Connection 으로부터 Cursor 생성
        cursor = admin_conn.cursor()

        # DB 로부터 테이블 목록(작물별 데이터셋) 을 가져옴
        show_tables_sql = "SHOW TABLES"

        cursor.execute(show_tables_sql)

        table_list = cursor.fetchall()
        table_list = [table[0] for table in table_list]
        print(table_list)

        # DB 로부터 테이블 정보로 column 명 리스트 생성
        desc_table_sql = "DESC %s" % table_list[0]
        cursor.execute(desc_table_sql)
        col_list = cursor.fetchall()
        col_list = [col[0] for col in col_list]
        print(col_list)

        # DB 로부터 작물별 모델을 생성함
        select_all_sql = "SELECT * FROM %s" % table_list[0]
        cursor.execute(select_all_sql)
        dataset = pd.DataFrame(list(cursor.fetchall()), columns=col_list)
        dataset.dropna(inplace=True)
        print(dataset)

        # LinearRegression model code
        linear_reg = LinearRegression()
        linear_reg.fit(dataset.drop(["region", "year", "prod"], axis=1), dataset["prod"])

        print(__file__)
        # "C:/Users/USER/PycharmProjects/FarmSolution/ML_API/farmsprings_api/models"
        path = os.path.join("../../../models", "test")
        with open(path, 'wb') as file:
            pickle.dump(linear_reg, file)


        # DB 로부터 데이터셋을 가져옴
        # insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, col_list_string, values_string)

        # cursor.execute(insert_sql)

        # connection 종료
        admin_conn.close()

if __name__ == "__main__":
    Command().handle()
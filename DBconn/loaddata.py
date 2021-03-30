import pymysql
import pandas as pd
import os

def insert_csv_to_db():
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

    # DB 의 테이블 특성과 그에 대응되는 csv 파일 데이터셋의 특성 (col : 특성명, 설명)
    featuer_df = pd.read_excel("features.xlsx")
    # sql 문에 들어갈 feature 명 문자열
    col_list_string = ", ".join(list(featuer_df["특성명"]))
    # print(col_list_string)

    # 데이터셋 파일별 DB 테이블명 (col : 파일명, 테이블명)
    table_name_df = pd.read_csv("작물별테이블명.csv", sep="\t")
    # print(table_name_df)

    # dataset 파일의 경로
    dir_path = "../PredictionModel/datasets/종관기상관측/default/"

    # 모든 데이터에 대하여 테이블 마다 INSERT 문 실행
    for file_name, table_name in zip(table_name_df["파일명"], table_name_df["테이블명"]):

        data_df = pd.read_csv(dir_path + file_name)

        print(file_name, "to", table_name)

        for _, row in data_df.iterrows():
            values_string = ",".join(map(str, [row[col_name]
                                               if col_name != "지역"
                                               else '"' + row[col_name] + '"'
                                               for col_name in featuer_df["설명"]
                                               ]))
            values_string = values_string.replace("nan", "NULL")

            insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, col_list_string, values_string)

            cursor.execute(insert_sql)

    # db의 변화 저장
    admin_conn.commit()

    # connection 종료
    admin_conn.close()

def insert_seg_csv_to_db():
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

    # DB 의 테이블 특성과 그에 대응되는 csv 파일 데이터셋의 특성 (col : 특성명, 설명)
    featuer_df = pd.read_csv("seg_features.csv")

    # sql 문에 들어갈 feature 명 문자열
    col_list_string = ", ".join(list(featuer_df["특성명"]))
    # print(col_list_string)

    # 데이터셋 파일별 DB 테이블명 (col : 파일명, 테이블명)
    table_name_df = pd.read_csv("작물별seg테이블명.csv", sep="\t")
    # print(table_name_df)

    # dataset 파일의 경로
    dir_path = "../PredictionModel/datasets/종관기상관측/default/"

    # 모든 데이터에 대하여 테이블 마다 INSERT 문 실행
    for file_name, table_name in zip(table_name_df["파일명"], table_name_df["테이블명"]):

        data_df = pd.read_csv(dir_path + file_name)

        print(file_name, "to", table_name)

        for _, row in data_df.iterrows():
            values_string = ",".join(map(str, [row[col_name]
                                               if col_name != "지역"
                                               else '"' + row[col_name] + '"'
                                               for col_name in featuer_df["설명"]
                                               ]))
            values_string = values_string.replace("nan", "NULL")

            insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, col_list_string, values_string)

            cursor.execute(insert_sql)

    # db의 변화 저장
    admin_conn.commit()

    # connection 종료
    admin_conn.close()

def insert_prod_area_to_db():
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

    # DB 의 테이블 특성과 그에 대응되는 csv 파일 데이터셋의 특성 (col : 특성명, 설명)
    features = ["region", "year", "prod", "area", "prod_per_area"]

    # sql 문에 들어갈 feature 명 문자열
    col_list_string = ", ".join(features)
    # print(col_list_string)

    # 데이터셋 파일별 DB 테이블명 (col : 파일명, 테이블명)
    table_name_df = pd.read_csv("작물별생산면적테이블명.csv", sep="\t")
    # print(table_name_df)

    # data 파일의 경로
    prod_dir_path = "../PreprocessingCropsData/농작물생산조사/preprocessed_prod_data/"
    area_dir_path = "../PreprocessingCropsData/농작물생산조사/preprocessed_area_data/"

    # 모든 데이터에 대하여 테이블 마다 INSERT 문 실행
    for crop_name, table_name in zip(table_name_df["작물명"], table_name_df["테이블명"]):

        print(crop_name, "to", table_name)

        prod_df = pd.read_csv(prod_dir_path + crop_name + "_생산량.csv")
        area_df = pd.read_csv(area_dir_path + crop_name + "_면적.csv")

        prod_df = prod_df[prod_df["시도별"] != "계"]
        area_df = area_df[area_df["시도별"] != "계"]

        sido_list = list(prod_df["시도별"])

        prod_df.set_index("시도별", inplace=True)
        area_df.set_index("시도별", inplace=True)

        year_list = list(prod_df.columns)

        for year in year_list:
            for sido in sido_list:
                prod_value = prod_df.loc[sido, year]
                area_value = area_df.loc[sido, year]

                print(prod_value, area_value)

                if (prod_value != 0) & (area_value != 0):
                    values_string = ",".join(["'" + sido + "'", year, str(prod_value), str(area_value), str(prod_value/area_value)])

                    insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, col_list_string, values_string)

                    print(insert_sql)

                    cursor.execute(insert_sql)

    # db의 변화 저장
    admin_conn.commit()

    # connection 종료
    admin_conn.close()

if __name__ == "__main__":
    # insert_csv_to_db()

    insert_seg_csv_to_db()

    # insert_prod_area_to_db()

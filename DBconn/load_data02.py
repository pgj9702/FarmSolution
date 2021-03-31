import pymysql
import pandas as pd
import os

def insert_csv_to_db():
    # MySQL Connection 연결
    admin_conn = pymysql.connect(
        user='root',
        password='1234',
        host='127.0.0.1',
        db='cropsdb',
        charset='utf8'
    )

    # Connection 으로부터 Cursor 생성
    cursor = admin_conn.cursor()

    # sql 문에 들어갈 feature 명 문자열
    col_list_string = "region, crop, area, avgTa, minTa, maxTa, hr1MaxRn, meanRn, sumRn, maxInsWs, maxWs, avgWs, hr24SumRws, avgTd , minRhm, avgRhm, avgPv, avgPa, ssDur, sumSsHr, hr1MaxIcsr, sumGsr, ddMefs, ddMes, avgTs, minTg, avgCm5Te, avgCm10Te, avgCm20Te, avgCm30Te, avgM05Te, avgM10Te, avgM15Te, avgM30Te, avgM50Te, meanDtr, numWdtr, numTyp, numImpT, sumCw, sumHw"

    data_df = pd.read_csv("weather_data.csv")

    feature = ["지역", "작물", "면적","평균 기온","최저 기온","최고 기온","1시간 최다강수량","일 강수량 평균","강수량 합계","최대 순간풍속",
               "최대 풍속","평균 풍속","풍정합","평균 이슬점온도","최소 상대습도","평균 상대습도","평균 증기압","평균 현지기압","가조시간",
               "평균 일조 시간","1시간 최다 일사량 평균","평균 일 합계 일사","일 최심신적설","일 최심적설","지면온도","최저 초상온도",
               "5cm 지중온도","10cm 지중온도","20cm 지중온도","30cm 지중온도","0.5m 지중온도","1.0m 지중온도","1.5m 지중온도",
               "3.0m 지중온도","5.0m 지중온도","평균 일교차","일교차 15이상인 날","태풍 수","영향을 준 태풍 수","한파일 수","폭염일 수"]

    for _, row in data_df.iterrows():
        values_string = ",".join(map(str, [row[col_name]
                                           if (col_name != "지역") and (col_name != "작물")
                                           else '"' + row[col_name] + '"'
                                           for col_name in feature
                                           ]))
        values_string = values_string.replace("nan", "NULL")

        insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % ("data_predict", col_list_string, values_string)


        cursor.execute(insert_sql)

    # db의 변화 저장
    admin_conn.commit()

    # connection 종료
    admin_conn.close()

def insert_seg_csv_to_db():
    # MySQL Connection 연결
    admin_conn = pymysql.connect(
        user='root',
        password='1234',
        host='127.0.0.1',
        db='cropsdb',
        charset='utf8'
    )

    # Connection 으로부터 Cursor 생성
    cursor = admin_conn.cursor()


    # sql 문에 들어갈 feature 명 문자열
    col_list_string = "region, crop, area, numImpT, 1_sumRn, 2_sumRn, 3_sumRn, 1_avgTa, 1_meanRn, 1_maxInsWs, 1_avgWs, 1_avgTd, 1_minRhm, 1_avgRhm, 1_avgPa, 1_ssDur, 1_sumSsHr, 1_hr1MaxIcsr, 1_ddMes, 1_avgTs, 1_minTg, 1_avgCm30Te, 1_avgM30Te, 2_avgTa, 2_meanRn, 2_maxInsWs, 2_avgWs, 2_avgTd, 2_minRhm, 2_avgRhm, 2_avgPa, 2_ssDur, 2_sumSsHr, 2_hr1MaxIcsr, 2_ddMes, 2_avgTs, 2_minTg, 2_avgCm30Te, 2_avgM30Te, 3_avgTa, 3_meanRn, 3_maxInsWs, 3_avgWs, 3_avgTd, 3_minRhm, 3_avgRhm, 3_avgPa, 3_ssDur, 3_sumSsHr, 3_hr1MaxIcsr, 3_ddMes, 3_avgTs, 3_minTg, 3_avgCm30Te, 3_avgM30Te, 1_meanDtr, 2_meanDtr, 3_meanDtr, 1_numWdtr, 2_numWdtr, 3_numWdtr, 1_sumCw, 2_sumCw, 3_sumCw, 1_sumHw, 2_sumHw, 3_sumHw"

    # 데이터셋 파일별 DB 테이블명 (col : 파일명, 테이블명)
    table_name_df = pd.read_csv("작물별seg테이블명.csv", sep="\t")
    # print(table_name_df)

    # dataset 파일의 경로
    dir_path = "../PredictionModel/datasets/종관기상관측/default/"

    data_df = pd.read_csv("weather_seg_data.csv")

    feature = ['지역', '작물', '면적', '영향을 준 태풍 수', '1분기 강수량 합계', '2분기 강수량 합계', '3분기 강수량 합계',
       '1분기 평균 기온', '1분기 일 강수량 평균', '1분기 최대 순간풍속', '1분기 평균 풍속', '1분기 평균 이슬점온도',
       '1분기 최소 상대습도', '1분기 평균 상대습도', '1분기 평균 현지기압', '1분기 가조시간', '1분기 평균 일조 시간',
       '1분기 1시간 최다 일사량 평균', '1분기 일 최심적설', '1분기 지면온도', '1분기 최저 초상온도',
       '1분기 30cm 지중온도', '1분기 3.0m 지중온도', '2분기 평균 기온', '2분기 일 강수량 평균',
       '2분기 최대 순간풍속', '2분기 평균 풍속', '2분기 평균 이슬점온도', '2분기 최소 상대습도',
       '2분기 평균 상대습도', '2분기 평균 현지기압', '2분기 가조시간', '2분기 평균 일조 시간',
       '2분기 1시간 최다 일사량 평균', '2분기 일 최심적설', '2분기 지면온도', '2분기 최저 초상온도',
       '2분기 30cm 지중온도', '2분기 3.0m 지중온도', '3분기 평균 기온', '3분기 일 강수량 평균',
       '3분기 최대 순간풍속', '3분기 평균 풍속', '3분기 평균 이슬점온도', '3분기 최소 상대습도',
       '3분기 평균 상대습도', '3분기 평균 현지기압', '3분기 가조시간', '3분기 평균 일조 시간',
       '3분기 1시간 최다 일사량 평균', '3분기 일 최심적설', '3분기 지면온도', '3분기 최저 초상온도',
       '3분기 30cm 지중온도', '3분기 3.0m 지중온도', '1분기 평균 일교차', '2분기 평균 일교차',
       '3분기 평균 일교차', '1분기 일교차 15이상인 날', '2분기 일교차 15이상인 날', '3분기 일교차 15이상인 날',
       '1분기 한파일 수', '2분기 한파일 수', '3분기 한파일 수', '1분기 폭염일 수', '2분기 폭염일 수',
       '3분기 폭염일 수']


    for _, row in data_df.iterrows():
        values_string = ",".join(map(str, [row[col_name]
                                           if (col_name != "지역") and (col_name != "작물")
                                           else '"' + row[col_name] + '"'
                                           for col_name in feature
                                           ]))
        values_string = values_string.replace("nan", "NULL")

        insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % ("seg_data_predict", col_list_string, values_string)

        cursor.execute(insert_sql)

    # db의 변화 저장
    admin_conn.commit()

    # connection 종료
    admin_conn.close()


if __name__ == "__main__":

    insert_csv_to_db()

    insert_seg_csv_to_db()



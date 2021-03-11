import numpy as np
import pandas as pd
import os
import datetime as dt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler


# 날짜 string format "yyyy-mm-dd" 를 datetime.date 형으로 변환'


def to_date_type(x):
    # x = "2000-01-31"
    temp = [int(i) for i in x.split("-")]
    return dt.date(temp[0], temp[1], temp[2])


def set_datasets(scaler=None):
    file_list = os.listdir("../../PreprocessingCropsData/농작물생산조사/preprocessed_area_data")

    file_list = [file.split("_") for file in file_list]

    crop_list = [file[0] + "_" + file[1] for file in file_list]

    # print(crop_list)

    # 작물별 생육기간 DataFrame
    growing_period = pd.read_csv("작물별 생육기간.csv")

    # 저장 경로 설정
    path_to_save = "../datasets/종관기상관측/"

    if scaler == "standard":
        path_to_save = path_to_save + "standard/"

    elif scaler == "robust":
        path_to_save = path_to_save + "robust/"

    elif scaler == "minmax":
        path_to_save = path_to_save + "minmax/"

    else:
        path_to_save = path_to_save + "default/"

    # 작물별 데이터셋 저장 파일명
    save_files = [crop + "_dataset.csv" for crop in crop_list]

    datasets_columns = [
        '지역', '시간', '평균 기온', '최저 기온', '최고 기온',
        '1시간 최다강수량', '일 강수량 평균', '강수량 합계', '최대 순간풍속', '최대 풍속', '평균 풍속',
        '풍정합', '평균 이슬점온도', '최소 상대습도', '평균 상대습도', '평균 증기압', '평균 현지기압',
        '가조시간', '합계 일조 시간', '1시간 최다 일사량', '합계 일사', '일 최심신적설', '일 최심적설',
        '평균 지면온도', '최저 초상온도', '평균 5cm 지중온도', '평균10cm 지중온도', '평균 20cm 지중온도', '평균 30cm 지중온도',
        '0.5m 지중온도', '1.0m 지중온도', '1.5m 지중온도', '3.0m 지중온도', '5.0m 지중온도'
    ]

    # 구간 별 통계 : '평균 기온', '최저 기온', '최고 기온, '일 강수량 평균', '강수량 합계', '평균 상대습도', '합계 일조 시간',
    # '평균 지면온도', '최저 초상온도', '평균 5cm 지중온도', '평균10cm 지중온도', '평균 20cm 지중온도', '평균 30cm 지중온도'

    for file_name in save_files:
        df_for_storage = pd.DataFrame(columns=datasets_columns)
        df_for_storage.to_csv(path_to_save + file_name, index=False, encoding="utf-8-sig")

    # 시도별 관측지점 DataFrame
    station_by_sido = pd.read_csv("시도별관측지점.csv", sep="\t").loc[8:, :]

    # int 형인 법정동코드를 str 형으로 바꾸어 날씨 데이터의 지역 코드와 광역시도 데이터의 지역 코드의 맨 앞 2자리를 비교하여
    # 지역 이름을 광역시도 이름으로 바꿈
    # ex) 강남구 -> 서울, 중구 -> 서울

    for sido, station in zip(station_by_sido["시도"], station_by_sido["지점"]):

        station_list = station.split(", ")

        weather_df_list = []

        for stat in station_list:
            weather_df_list.append(
                pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/일기상자료_" +
                            stat +
                            "_2001_2019.csv"))

        # 시도에 해당하는 관측지점 데이터를 통합
        weather_df = pd.concat([df for df in weather_df_list], ignore_index=True)

        weather_df.drop(["지점 번호", "지점명"], inplace=True, axis=1)

        weather_df.sort_values(by=["시간"], inplace=True, ignore_index=True)

        # 같은 날짜 별로 그룹화 후 평균
        weather_df_mean = weather_df.groupby(by=["시간"], as_index=False).mean()

        # print(weather_df)

        for crop in crop_list:
            # 작물 생산량 데이터
            crop_prod_data = pd.read_csv("../../PreprocessingCropsData/농작물생산조사/preprocessed_prod_data/" + crop + "_생산량.csv")
    
            # 작물 면적 데이터
            crop_area_data = pd.read_csv("../../PreprocessingCropsData/농작물생산조사/preprocessed_area_data/" + crop + "_면적.csv")
            
            for year in range(2001, 2020):

                # 작물별 생육 기간
                crop_growing_period = growing_period[(growing_period["품목"] == crop.split("_")[0])
                                                     & (growing_period["품종"] == crop.split("_")[1])]

                start_md = crop_growing_period["생육시작"].values[0].split("-")
                end_md = crop_growing_period["생육종료"].values[0].split("-")

                print(crop)
                print(start_md, end_md)

                if start_md[0] != "":
                    s_year, s_month, s_day = 2000, int(start_md[0]), int(start_md[1])
                else:
                    s_year, s_month, s_day = 2000, 1, 1

                e_year, e_month, e_day = 2000, int(end_md[0]), int(end_md[1])

                start_md = dt.date(s_year, s_month, s_day)
                end_md = dt.date(e_year, e_month, e_day)

                final_df = pd.DataFrame(columns=datasets_columns)

                region_list = preprocessing_df["지역 이름"].unique()

                print(weather_df_mean)
                # print("생산량 면적 확인")
                # print(prod_data[prod_data["시도별"] == area][str(year)].values[0])
                # print(area_data[prod_data["시도별"] == area][str(year)].values[0])
                a = ['시간', '평균 기온', '최저 기온', '최고 기온', '1시간 최다강수량', '일강수량', '최대 순간풍속',
       '최대 풍속', '평균 풍속', '풍정합', '평균 이슬점온도', '최소 상대습도', '평균 상대습도', '평균 증기압',
       '평균 현지기압', '가조시간', '합계 일조 시간', '1시간 최다 일사량', '합계 일사', '일 최심신적설',
       '일 최심적설', '평균 지면온도', '최저 초상온도', '평균 5cm 지중온도', '평균10cm 지중온도',
       '평균 20cm 지중온도', '평균 30cm 지중온도', '0.5m 지중온도', '1.0m 지중온도', '1.5m 지중온도',
       '3.0m 지중온도', '5.0m 지중온도']

                datasets_columns = [
                    '지역', '시간', '평균 기온', '최저 기온', '최고 기온',
                    '1시간 최다강수량', '일 강수량 평균', '강수량 합계', '최대 순간풍속', '최대 풍속', '평균 풍속',
                    '풍정합', '평균 이슬점온도', '최소 상대습도', '평균 상대습도', '평균 증기압', '평균 현지기압',
                    '가조시간', '합계 일조 시간', '1시간 최다 일사량', '합계 일사', '일 최심신적설', '일 최심적설',
                    '평균 지면온도', '최저 초상온도', '평균 5cm 지중온도', '평균10cm 지중온도', '평균 20cm 지중온도', '평균 30cm 지중온도',
                    '0.5m 지중온도', '1.0m 지중온도', '1.5m 지중온도', '3.0m 지중온도', '5.0m 지중온도'
                ]

                values_of_new_row = [sido, year,
                                     crop_prod_data[str(year)].values[0],
                                     crop_area_data[str(year)].values[0],
                                     temp_df02['일 평균기온'].mean(),
                                     temp_df02['일 최저기온'].mean(),
                                     temp_df02['일 최고기온'].mean(),
                                     temp_df02['일 평균풍속'].mean(),
                                     temp_df02['일 평균상대습도'].mean(),
                                     temp_df02['일 최저상대습도'].mean(),
                                     temp_df02['일 강수량'].mean(),
                                     temp_df02['일 누적일조시간'].mean()
    
                                     # temp_df02['태풍'].mean(),
                                     # temp_df02['일교차'].mean(),
                                     # temp_df02['일교차 10 이상'].mean(),
                                     # temp_df02['한파 일 수'].mean(),
                                     # temp_df02['폭염 일 수'].mean()
                                     ]
    
                new_row = {key: value for key, value in zip(datasets_columns, values_of_new_row)}

                # excel 파일에 이어서 저장
                new_row.to_csv(path_to_save + crop + "_dataset.csv", mode="a", header=False,
                                index=False, encoding="utf-8-sig")
            



    for crop in crop_list:

        print(crop, "  data set ")

        weather_data = pd.read_csv(
            "../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_crops_weather_data/일기상자료" + crop + "_날씨.csv")

        # 년-월-일 시:분:초 를 년-월-일 로 변경
        weather_data["연월일"] = weather_data["연월일"].str.split().str[0]

        # print(weather_data)

        # print(weather_data.columns)

        # '태풍', '일교차', '일교차 10 이상', '한파 일 수', '폭염 일 수',

        # scaler 적용

        # scaler 를 적용할 columns

        col_to_scale = ["일 평균상대습도", "일 평균기온", "일 평균풍속", "일 최고기온", "일 최저상대습도", "일 최저기온", "일 강수량", "일 누적일조시간"]
        # scaler

        if scaler == "standard":
            standard_scaler = StandardScaler()
            standard_scaler.fit(weather_data[col_to_scale])
            weather_data[col_to_scale] = standard_scaler.transform(weather_data[col_to_scale])

        elif scaler == "robust":
            robust_scaler = RobustScaler()
            robust_scaler.fit(weather_data[col_to_scale])
            weather_data[col_to_scale] = robust_scaler.transform(weather_data[col_to_scale])

        elif scaler == "minmax":
            min_max_scaler = MinMaxScaler()
            min_max_scaler.fit(weather_data[col_to_scale])
            weather_data[col_to_scale] = min_max_scaler.transform(weather_data[col_to_scale])

        datasets_columns = ['지역 이름', '년도', '생산량', '면적', '일 평균기온', '일 최저기온', '일 최고기온', '일 평균풍속',
                            '일 평균상대습도', '일 최저상대습도', '일 강수량', '일 누적일조시간']

        # ********* 지역 통합 *********

        preprocessing_df = weather_data.copy()

        preprocessing_df = preprocessing_df.drop(['작물 명', '작물별 특성아이디', '작물별 특성 이름', '특보 코드', '특보 발효 여부'], axis=1)

        preprocessing_df["지역 아이디"] = preprocessing_df["지역 아이디"].astype("str")

        # preprocessed_df['지역 이름'] = preprocessed_df[preprocessed_df["지역 아이디"].str[:2].contain()]

        preprocessing_df['지역 이름'] = [list(sido_code[sido_code["법정동코드"] == row["지역 아이디"][:2]]["법정동명"])[0]
                                     if row["지역 아이디"][:2] in sido_code["법정동코드"].values
                                     else "세종특별자치시"
        if row["지역 아이디"][:4] == sido_code[sido_code["법정동명"] == "세종특별자치시"]["법정동코드"].values[0]
        else None
                                     for _, row in preprocessing_df.iterrows()]

        preprocessing_df.drop("지역 아이디", axis=1, inplace=True)

        # print(preprocessing_df)

        # ********* 날짜 통합 *********

        # print(growing_period)

        # 작물별 생육 기간
        crop_growing_period = growing_period[(growing_period["품목"] == crop.split("_")[0])
                                             & (growing_period["품종"] == crop.split("_")[1])]

        start_md = crop_growing_period["생육시작"].values[0].split("-")
        end_md = crop_growing_period["생육종료"].values[0].split("-")

        if start_md[0] != "":
            s_year, s_month, s_day = 2000, int(start_md[0]), int(start_md[1])
        else:
            s_year, s_month, s_day = 2000, 1, 1

        e_year, e_month, e_day = 2000, int(end_md[0]), int(end_md[1])

        start_md = dt.date(s_year, s_month, s_day)
        end_md = dt.date(e_year, e_month, e_day)

        final_df = pd.DataFrame(columns=datasets_columns)

        region_list = preprocessing_df["지역 이름"].unique()

        # 생산량, 면적 csv 파일 읽기

        prod_data = pd.read_csv("../../PreprocessingCropsData/농작물생산조사/preprocessed_prod_data/" + crop + "_생산량.csv")
        area_data = pd.read_csv("../../PreprocessingCropsData/농작물생산조사/preprocessed_area_data/" + crop + "_면적.csv")

        # print(prod_data)
        # print(prod_data.columns)
        # print(area_data)
        # print(area_data.columns)

        for region in region_list:
            temp_df01 = preprocessing_df[preprocessing_df["지역 이름"] == region]
            # print(temp_df01)

            # 특정 지역의
            date_series = temp_df01["연월일"].apply(to_date_type)

            min_year = int((np.min(temp_df01["연월일"]))[:4])

            max_year = int((np.max(temp_df01["연월일"]))[:4])

            print(region, min_year, "~", max_year)

            year_range = range(min_year, max_year + 1)

            for year in year_range:
                start_ymd = dt.date(year, start_md.month, start_md.day)
                end_ymd = dt.date(year, end_md.month, end_md.day)

                region_prod_data = prod_data[prod_data["시도별"] == region]
                region_area_data = area_data[area_data["시도별"] == region]

                if str(year) not in region_prod_data.columns or str(year) not in region_area_data.columns:
                    continue


                elif start_ymd in date_series.values and end_ymd in date_series.values:
                    # print("good")

                    if start_ymd > end_ymd:
                        if year == 2001:
                            continue
                        else:
                            start_ymd = dt.date(year - 1, start_md.month, start_md.day)

                    temp_df02 = temp_df01[(date_series >= start_ymd) & (date_series <= end_ymd)]

                else:
                    # print("break")
                    # print(start_ymd, end_ymd)
                    # print(date_series.values[0], date_series.values[len(date_series)-1])

                    # 다음 year 로 넘어감
                    continue

                # print(date_in_growing_period, len(date_in_growing_period))
                #
                # print(start_ymd, end_ymd)
                #
                # print("일 수 :", end_ymd - start_ymd + dt.timedelta(days=1))

                # temp_df01.columns

                # ['지역 이름', '년도', '생산량', '면적', '일 평균기온', '일 최저기온', '일 최고기온', '일 평균풍속', '일 평균상대습도',
                # '일 최저상대습도', '일 강수량', '일 누적일조시간', '태풍', '일교차', '일교차 10 이상', '한파 일 수', '폭염 일 수']

                # datasets_columns
                # '지역 이름', '년도', '일 평균기온', '일 최저기온', '일 최고기온', '일 평균풍속', '일 평균상대습도',
                # '일 최저상대습도', '일 강수량', '일 누적일조시간', '한파 일 수', '폭염 일 수'
                # 추가할 col : 태풍 수, 일교차(하루 최고 기온과 최저 기온 차, 일교차가 큰 날)?

                # 한파
                # 10월~4월 동안 다음 어느 하나에 해당하는 경우
                # ① 아침 최저기온이 전날보다 10℃ 이상 하강하여 3℃ 이하이고 평년값보다 3℃가 낮을 것으로 예상될 때
                # ② 아침 최저기온이 -12℃ 이하가 2일 이상 지속될 것으로 예상될 때
                # ③ 급격한 저온현상으로 중대한 피해가 예상될 때

                # 폭염
                # 일최고기온이 33℃ 이상인 상태가 2일 이상 지속될 것으로 예상될 때

                # 한파
                # cold_wave = ??

                # 폭염
                # heat_wave = ??

                # 같은 날짜 여러 row 를 하나로 통합
                temp_df02 = temp_df02.groupby(by=["연월일"], as_index=False).mean()

                print(temp_df02)
                # print("생산량 면적 확인")
                # print(prod_data[prod_data["시도별"] == area][str(year)].values[0])
                # print(area_data[prod_data["시도별"] == area][str(year)].values[0])

                values_of_new_row = [region, year,
                                     region_prod_data[str(year)].values[0],
                                     region_area_data[str(year)].values[0],
                                     temp_df02['일 평균기온'].mean(),
                                     temp_df02['일 최저기온'].mean(),
                                     temp_df02['일 최고기온'].mean(),
                                     temp_df02['일 평균풍속'].mean(),
                                     temp_df02['일 평균상대습도'].mean(),
                                     temp_df02['일 최저상대습도'].mean(),
                                     temp_df02['일 강수량'].mean(),
                                     temp_df02['일 누적일조시간'].mean()

                                     # temp_df02['태풍'].mean(),
                                     # temp_df02['일교차'].mean(),
                                     # temp_df02['일교차 10 이상'].mean(),
                                     # temp_df02['한파 일 수'].mean(),
                                     # temp_df02['폭염 일 수'].mean()
                                     ]

                new_row = {key: value for key, value in zip(datasets_columns, values_of_new_row)}

                final_df = final_df.append(new_row, ignore_index=True)

        final_df.sort_values(by=["년도"], inplace=True)
        final_df.to_csv(path_to_save + crop + "_dataset.csv", index=False, encoding="utf-8-sig")
        # excel 파일에 이어서 저장
        # df.to_csv(file_name, mode="a", header=False, index=False, encoding="utf-8-sig")


if __name__ == "__main__":

    # 법정동코드에서 광역시도 코드만 정리하여 csv 파일롤 저장
    # save_sido_csv()

    scalers = ["default", "standard", "robust", "minmax"]

    set_datasets()

    # for scaler in scalers:
    #     preprocessing_datasets(scaler=scaler)

        # temp_df["연월일"]
        #
        # for i, v in date_series.items():
        #     print(i, type(v))
        #
        # print(pd.to_datetime(start_md))
        # print(pd.to_datetime(end_md))

        # print(pd.to_datetime(temp_df["연월일"])[7113])
        # print(pd.to_datetime(temp_df["연월일"])[7113] + pd.to_timedelta("1 days"))

        # year_list = list(set(temp_df["연월일"].str.split("-").str[0]))
        #
        # year_list.sort()
        #
        # print(year_list)

        # for year in year_list:
        #     print(year)

        # '지역 이름', '년도', '일 최저기온', '일 평균기온', '일 최고기온', '일 평균풍속', '일 평균상대습도', '일 최저상대습도', '일 강수량', '일 누적일조시간', '한파 일 수', '폭염 일 수'

        # values_of_new_row = [area, ]
        #
        # new_row = {key: value for key, value in zip(datasets_columns, values_of_new_row)}
        #
        # final_df.append(new_row, ignore_index=True)




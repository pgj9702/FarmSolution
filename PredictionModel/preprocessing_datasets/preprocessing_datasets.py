import numpy as np
import pandas as pd
import os
import datetime as dt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

# 법정동 지역 코드에서 광역시도 코드만 csv 파일로 저장하는 함수
def save_sido_csv():
    area_code = pd.read_csv("법정동코드 전체자료.txt", sep="\t")

    area_name_list = area_code["법정동명"].str.split()

    idx_list = []

    for i, v in area_name_list.items():
        if len(v) == 1:
            idx_list.append(i)

    sido_code = area_code.iloc[idx_list, :]
    sido_code = sido_code[sido_code["폐지여부"] == "존재"]

    sido_code["법정동코드"] = sido_code["법정동코드"].astype("str")

    sido_code["법정동코드"] = [row["법정동코드"][:2]
                          if row["법정동명"] != "세종특별자치시"
                          else row["법정동코드"][:4]
                          for _, row in sido_code.iterrows()]

    # 생산량, 면적 데이터에서는 "제주도" 라고 표기되어 있음
    # 법정동코드 전체자료.txt 파일에 "제주특별차지도" 를 "제주도" 로 수정하여 저장
    sido_code.loc[sido_code["법정동명"] == "제주특별자치도", "법정동명"] = "제주도"

    sido_code.to_csv("광역시도 코드.csv", index=False)


# 날짜 string format "yyyy-mm-dd" 를 datetime.date 형으로 변환'



def to_date_type(x):
    # x = "2000-01-31"
    temp = [int(i) for i in x.split("-")]
    return dt.date(temp[0], temp[1], temp[2])


def preprocessing_datasets(scaler=None):

    file_list = os.listdir("../../PreprocessingCropsData/농작물생산조사/preprocessed_area_data")

    # 당근 대파 양배추 마늘은 제외함
    for file in ['당근_-_면적.csv', '대파_-_면적.csv', '양배추_-_면적.csv', '마늘_-_면적.csv']:
        file_list.remove(file)

    # 베추_겨울

    file_list = [file.split("_") for file in file_list]

    crop_list = [file[0] + "_" + file[1] for file in file_list]

    # print(crop_list)

    # 작물별 생육기간 DataFrame
    growing_period = pd.read_csv("작물별 생육기간.csv")

    # 저장 경로 설정
    path_to_save = "../datasets/"

    if scaler == "standard":
        path_to_save = path_to_save + "standard/"

    elif scaler == "robust":
        path_to_save = path_to_save + "robust/"

    elif scaler == "minmax":
        path_to_save = path_to_save + "minmax/"

    else:
        path_to_save = path_to_save + "default/"

    # 광역시도 코드 DataFrame
    sido_code = pd.read_csv("광역시도 코드.csv")

    # int 형인 법정동코드를 str 형으로 바꾸어 날씨 데이터의 지역 코드와 광역시도 데이터의 지역 코드의 맨 앞 2자리를 비교하여
    # 지역 이름을 광역시도 이름으로 바꿈
    # ex) 강남구 -> 서울, 중구 -> 서울
    sido_code["법정동코드"] = sido_code["법정동코드"].astype("str")

    # print(sido_code)

    for crop in crop_list:

        print(crop, "  data set ")

        weather_data = pd.read_csv(
            "../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/" + crop + "_날씨.csv")

        # 년-월-일 시:분:초 를 년-월-일 로 변경
        weather_data["연월일"] = weather_data["연월일"].str.split().str[0]

        # print(weather_data)

        # print(weather_data.columns)

        # , '태풍', '일교차', '일교차 10 이상', '한파 일 수', '폭염 일 수',

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



if __name__ == "__main__":

    # 법정동코드에서 광역시도 코드만 정리하여 csv 파일롤 저장
    # save_sido_csv()

    scalers = ["default", "standard", "robust", "minmax"]

    preprocessing_datasets()

    for scaler in scalers:
        preprocessing_datasets(scaler=scaler)



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





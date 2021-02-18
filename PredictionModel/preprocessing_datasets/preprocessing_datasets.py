import pandas as pd
import os
import datetime as dt

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

    sido_code.to_csv("광역시도 코드.csv", index=False)

def preprocessing_datasets():
    weather_file_list = os.listdir("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data")

    weather_data = pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/감귤_-_날씨.csv")

    print(weather_data)


def func(x):
    print(x)


if __name__ == "__main__":
    
    # 법정동코드에서 광역시도 코드만 정리하여 csv 파일롤 저장
    # save_sido_csv()

    # preprocessing_datasets()

    file_list = os.listdir("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data")

    file_list = [file.split("_") for file in file_list]

    crop_list = [file[0] + "_" + file[1] for file in file_list]

    print(crop_list)

    crop = crop_list[0]

    weather_data = pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/" + crop + "_날씨.csv")

    # 년-월-일 시:분:초 를 년-월-일 로 변경
    weather_data["연월일"] = weather_data["연월일"].str.split().str[0]

    # print(weather_data)

    # print(weather_data.columns)

    weather_df_columns = ['지역 아이디', '지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속', '일 최고기온', '일 최저상대습도',
                          '일 최저기온', '일 강수량', '일 누적일조시간', '작물 명', '작물별 특성아이디', '작물별 특성 이름',
                          '특보 코드', '특보 발효 여부', '연월일']

    datasets_columns = ['지역 이름', '년도', '일 최저기온', '일 평균기온', '일 최고기온', '일 평균풍속',
                        '일 평균상대습도', '일 최저상대습도', '일 강수량', '일 누적일조시간', '한파 일 수', '폭염 일 수']

    # ********* 지역 통합 *********

    preprocessing_df = weather_data.copy()

    preprocessing_df = preprocessing_df.drop(['작물 명', '작물별 특성아이디', '작물별 특성 이름', '특보 코드', '특보 발효 여부'], axis=1)

    preprocessing_df["지역 아이디"] = preprocessing_df["지역 아이디"].astype("str")

    # preprocessed_df['지역 이름'] = preprocessed_df[preprocessed_df["지역 아이디"].str[:2].contain()]

    sido_code = pd.read_csv("광역시도 코드.csv")

    # int 형인 법정동코드를 str 형으로 바꾸어 날씨 데이터의 지역 코드와 광역시도 데이터의 지역 코드의 맨 앞 2자리를 비교하여
    # 지역 이름을 광역시도 이름으로 바꿈
    # ex) 강남구 -> 서울, 중구 -> 서울
    sido_code["법정동코드"] = sido_code["법정동코드"].astype("str")

    print(sido_code)

    preprocessing_df['지역 이름'] = [list(sido_code[sido_code["법정동코드"] == row["지역 아이디"][:2]]["법정동명"])[0]
                                if row["지역 아이디"][:2] in sido_code["법정동코드"].values
                                else "세종특별자치시"
                                if row["지역 아이디"][:4] == sido_code[sido_code["법정동명"] == "세종특별자치시"]["법정동코드"].values[0]
                                else None
                                 for _, row in preprocessing_df.iterrows()]

    preprocessing_df.drop("지역 아이디", axis=1, inplace=True)

    print(preprocessing_df)

    # ********* 날짜 통합 *********

    growing_period = pd.read_csv("작물별 생육기간.csv")

    print(growing_period)

    day = dt.date(day=10, month=10, year=2000)

    test = day - dt.timedelta(days=366)

    # 작물별 생육 기간

    start_md = growing_period[(growing_period["품목"] == crop.split("_")[0])
                              & (growing_period["품종"] == crop.split("_")[1])]["생육시작"].values[0]
    end_md = growing_period[(growing_period["품목"] == crop.split("_")[0])
                              & (growing_period["품종"] == crop.split("_")[1])]["생육종료"].values[0]

    print(start_md)
    print(end_md)

    final_df = pd.DataFrame(columns=datasets_columns)

    area_list = list(set(preprocessing_df["지역 이름"]))

    for area in area_list:
        temp_df = preprocessing_df[preprocessing_df["지역 이름"] == area]
        print(temp_df)

        year_list = list(set(temp_df["연월일"]))

        print(year_list)

        # for year in year_list:
        #     print(year)

        # '지역 이름', '년도', '일 최저기온', '일 평균기온', '일 최고기온', '일 평균풍속', '일 평균상대습도', '일 최저상대습도', '일 강수량', '일 누적일조시간', '한파 일 수', '폭염 일 수'

        # values_of_new_row = [area, ]
        #
        # new_row = {key: value for key, value in zip(datasets_columns, values_of_new_row)}
        #
        # final_df.append(new_row, ignore_index=True)

    # 한파
    # 10월~4월 동안 다음 어느 하나에 해당하는 경우
    # ① 아침 최저기온이 전날보다 10℃ 이상 하강하여 3℃ 이하이고 평년값보다 3℃가 낮을 것으로 예상될 때
    # ② 아침 최저기온이 -12℃ 이하가 2일 이상 지속될 것으로 예상될 때

    # ③ 급격한 저온현상으로 중대한 피해가 예상될 때

    # 폭염
    # 일최고기온이 33℃ 이상인 상태가 2일 이상 지속될 것으로 예상될 때



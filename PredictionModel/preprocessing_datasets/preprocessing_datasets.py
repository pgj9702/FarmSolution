import pandas as pd
import os


def preprocessing_datasets():
    weather_file_list = os.listdir("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data")

    weather_data = pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/감귤_-_날씨.csv")

    print(weather_data)


def func(x):
    print(x)


if __name__ == "__main__":
    # preprocessing_datasets()

    file_list = os.listdir("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data")

    # print(file_list)

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

    print(sido_code)

    weather_data = pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/감귤_-_날씨.csv")

    # 년-월-일 시:분:초 를 년-월-일 로 변경
    weather_data["연월일"] = weather_data["연월일"].str.split().str[0]

    print(weather_data)

    print(weather_data.columns)

    weather_df_columns = ['지역 아이디', '지역 이름', '일 평균상대습도', '일 평균기온', '일 평균풍속', '일 최고기온', '일 최저상대습도',
                          '일 최저기온', '일 강수량', '일 누적일조시간', '작물 명', '작물별 특성아이디', '작물별 특성 이름',
                          '특보 코드', '특보 발효 여부', '연월일']

    datasets_columns = ['지역 이름', '년도', '일 최저기온', '일 평균기온', '일 최고기온', '일 평균풍속',
                        '일 평균상대습도', '일 최저상대습도', '일 강수량', '일 누적일조시간', '한파 일 수', '폭염 일 수']

    # 한파
    # 10월~4월 동안 다음 어느 하나에 해당하는 경우
    # ① 아침 최저기온이 전날보다 10℃ 이상 하강하여 3℃ 이하이고 평년값보다 3℃가 낮을 것으로 예상될 때
    # ② 아침 최저기온이 -12℃ 이하가 2일 이상 지속될 것으로 예상될 때

    # ③ 급격한 저온현상으로 중대한 피해가 예상될 때

    # 폭염
    # 일최고기온이 33℃ 이상인 상태가 2일 이상 지속될 것으로 예상될 때

    preprocessed_df = weather_data.copy()

    preprocessed_df = preprocessed_df.drop(['작물 명', '작물별 특성아이디', '작물별 특성 이름', '특보 코드', '특보 발효 여부'], axis=1)

    preprocessed_df["지역 아이디"] = preprocessed_df["지역 아이디"].astype("str")

    # preprocessed_df['지역 이름'] = preprocessed_df[preprocessed_df["지역 아이디"].str[:2].contain()]

    preprocessed_df['지역 이름'] = [list(sido_code[sido_code["법정동코드"] == row["지역 아이디"][:2]]["법정동명"])[0]
                                if row["지역 아이디"][:2] in sido_code["법정동코드"].values
                                else "세종특별자치시"
                                if row["지역 아이디"][:4] == sido_code[sido_code["법정동명"] == "세종특별자치시"]["법정동코드"].values[0]
                                else None
                                for _, row in preprocessed_df.iterrows()]

    preprocessed_df.drop("지역 아이디", axis=1, inplace=True)

    print(preprocessed_df)

    # 작물별 생육 기간
    start_md = ""
    end_md = ""

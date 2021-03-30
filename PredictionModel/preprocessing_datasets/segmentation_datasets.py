import datetime as dt
import os

import pandas as pd


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
    save_files = [crop + "_seg_dataset.csv" for crop in crop_list]

    datasets_columns = [
                           '지역', '년도', '생산량', '면적', '영향을 준 태풍 수'
                       ] + \
                       ["%d분기 %s" % (num, '강수량 합계') for num in range(1, 4)] + \
                       ["%d분기 %s" % (num, feature) for num in range(1, 4)
                        for feature in
                        ['평균 기온', '일 강수량 평균', '최대 순간풍속', '평균 풍속',
                         '평균 이슬점온도', '최소 상대습도', '평균 상대습도', '평균 현지기압',
                         '가조시간', '평균 일조 시간', '1시간 최다 일사량 평균', '일 최심적설',
                         '지면온도', '최저 초상온도', '30cm 지중온도', '3.0m 지중온도']
                        ] + \
                       ["%d분기 %s" % (num, feature)
                        for feature in ['평균 일교차', '일교차 15이상인 날', '한파일 수', '폭염일 수']
                        for num in range(1, 4)
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

    # 태풍 DataFrame
    typhoon_df = pd.read_csv("../../PreprocessingCropsData/농업주산지상세날씨/typhoon/typhoon.csv")

    typhoon_df.fillna(0, inplace=True)
    typhoon_df.set_index("연월일", inplace=True)

    # 괄호 안의 숫자는 우리나라에 영향을 크게 미친 태풍 수
    # print(typhoon_df)

    typhoon_df.fillna(0, inplace=True)

    typhoon_df = typhoon_df.loc["2001":"2020", :]

    typhoon_df = typhoon_df.astype(str)

    typhoon_df = typhoon_df.apply(lambda x: x.str.replace(".0", "", regex=False))

    impact_typhoon_df = typhoon_df.apply(lambda x: x.str.split("(").str[1])

    impact_typhoon_df.fillna(0, inplace=True)

    impact_typhoon_df = impact_typhoon_df.astype(str)

    impact_typhoon_df = impact_typhoon_df.apply(lambda x: x.str.replace(")", "", regex=False))

    impact_typhoon_df = impact_typhoon_df.apply(lambda x: x.str.replace(".0", "", regex=False))

    typhoon_df = typhoon_df.apply(lambda x: x.str.split("(").str[0])

    # 태풍 개수
    typhoon_df = typhoon_df.astype(int)

    # 영향을 크게 미친 태풍 개수
    impact_typhoon_df = impact_typhoon_df.astype(int)

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
        daily_waether = weather_df.groupby(by=["시간"], as_index=False).mean()

        # str 타입의 날짜를 datetime.date 으로 변환한 Series
        date_series = daily_waether["시간"].apply(to_date_type)

        col_list_of_wth = ['평균 기온', '일강수량', '최대 순간풍속','평균 풍속',
                           '평균 이슬점온도', '최소 상대습도', '평균 상대습도', '평균 현지기압',
                           '가조시간', '합계 일조 시간', '1시간 최다 일사량', '일 최심적설',
                           '평균 지면온도', '최저 초상온도', '평균 30cm 지중온도', '3.0m 지중온도']

        for crop in crop_list:
            # 작물 생산량 데이터
            crop_prod_data = pd.read_csv(
                "../../PreprocessingCropsData/농작물생산조사/preprocessed_prod_data/" + crop + "_생산량.csv")
            crop_prod_data.set_index("시도별", inplace=True)

            # 작물 면적 데이터
            crop_area_data = pd.read_csv(
                "../../PreprocessingCropsData/농작물생산조사/preprocessed_area_data/" + crop + "_면적.csv")
            crop_area_data.set_index("시도별", inplace=True)

            for year in range(2001, 2020):
                str_year = str(year)

                # 생산량 정보
                if str_year not in crop_prod_data.columns:
                    print("continue")
                    continue

                # sido 의 year 해의 생산량이나 면적이 0이면 continue
                prod_of_sido_in_year = crop_prod_data.at[sido, str_year]
                area_of_sido_in_year = crop_area_data.at[sido, str_year]

                if prod_of_sido_in_year == 0 or area_of_sido_in_year == 0:
                    continue

                # 작물별 생육 기간
                crop_growing_period = growing_period[(growing_period["품목"] == crop.split("_")[0])
                                                     & (growing_period["품종"] == crop.split("_")[1])]

                start_md = crop_growing_period["생육시작"].values[0].split("-")
                end_md = crop_growing_period["생육종료"].values[0].split("-")

                print(crop)
                print(start_md, end_md)

                if start_md[0] != "":
                    s_year, s_month, s_day = year, int(start_md[0]), int(start_md[1])
                else:
                    s_year, s_month, s_day = year, 1, 1

                e_year, e_month, e_day = year, int(end_md[0]), int(end_md[1])

                start_ymd = dt.date(s_year, s_month, s_day)
                end_ymd = dt.date(e_year, e_month, e_day)

                if start_ymd > end_ymd:
                    if year == 2001:
                        continue
                    else:
                        start_ymd = dt.date(year - 1, start_ymd.month, start_ymd.day)

                temp_df01 = daily_waether[(date_series >= start_ymd) &
                                          (date_series <= end_ymd)]

                # 일교차
                daily_tp_range = temp_df01["최고 기온"] - temp_df01["최저 기온"]

                # print("생산량 면적 확인")
                # print(prod_data[prod_data["시도별"] == area][str(year)].values[0])
                # print(area_data[prod_data["시도별"] == area][str(year)].values[0])

                # print(col_list_of_wth)

                # 한파
                # 10월~4월 동안 다음 어느 하나에 해당하는 경우
                # 1. 최저기온이 전날보다 10℃ 이상 하강하여 3℃ 이하인 경우
                # 2. 최저기온이 -12℃ 이하가 2일 이상 지속될 것으로 예상될 때

                # 작년에 파종하여 올해 수확하는 경우
                count_cw_list = []
                count_hw_list = []
                daily_tp_range_over_10 = []
                weather_df_section = []
                daily_tp_range_list = []

                date_series_temp = date_series[(date_series >= start_ymd) &
                                               (date_series <= end_ymd)]

                # 3분기로 분할
                len_section = len(date_series_temp.index) // 3

                for date_section in [
                    date_series_temp[:len_section],
                    date_series_temp[len_section:len_section * 2],
                    date_series_temp[len_section * 2:]
                ]:

                    if start_ymd.year != end_ymd.year:

                        cw_df = daily_waether.iloc[
                            list(((date_section >= dt.date(start_ymd.year, 10, 1)) &
                            (date_section < dt.date(end_ymd.year, 5, 1))).index)
                        ]["최저 기온"]

                        cw_section01 = cw_df[cw_df <= 3.0]

                        cw_section01_eve = daily_waether.iloc[cw_section01.index - 1]["최저 기온"]

                        cw_section01.reset_index(inplace=True, drop=True)
                        cw_section01_eve.reset_index(inplace=True, drop=True)

                        # 12도 이하가 2일 유지되거나 3도 이하이면서 전날보다 10도 이상 하강한 경우
                        # 작년10월부터 올해4월까지
                        cold_continuing01 = pd.DataFrame([cw_section01 <= -12.0, cw_section01_eve <= -12.0]).all()

                        # 최저기온이 전날보다 10℃ 이상 하강하여 3℃ 이하일 때
                        # 두 조건 중 하나만 만족하는 날
                        # 작년10월부터 올해4월까지
                        section01_list = pd.DataFrame([cold_continuing01, (cw_section01 - cw_section01_eve <= -10.0)]).any()

                        # 한파 일수 cold_wave
                        count_cw_list.append(section01_list.sum())

                    else:
                        cw_df = daily_waether.iloc[list((((date_section >= dt.date(year, 1, 1)) &
                                                     (date_section < dt.date(year, 5, 1))) |
                                                ((date_section >= dt.date(year, 10, 1)) &
                                                 (date_section < dt.date(year + 1, 1, 1)))).index)
                        ]["최저 기온"]

                        cw_section01 = cw_df[cw_df <= 3.0]

                        cw_section01_eve = daily_waether.iloc[cw_section01.index - 1]["최저 기온"]

                        cw_section01.reset_index(inplace=True, drop=True)
                        cw_section01_eve.reset_index(inplace=True, drop=True)

                        # 12도 이하가 2일 유지되거나 3도 이하이면서 전날보다 10도 이상 하강한 경우
                        cold_continuing01 = pd.DataFrame([cw_section01 <= -12.0, cw_section01_eve <= -12.0]).all()

                        # 최저기온이 전날보다 10℃ 이상 하강하여 3℃ 이하일 때
                        # 두 조건 중 하나만 만족하는 날
                        section01_list = pd.DataFrame([cold_continuing01, (cw_section01 - cw_section01_eve <= -10.0)]).any()

                        # 한파 일수 cold_wave
                        count_cw_list.append(section01_list.sum())

                    # 폭염
                    # 최고기온이 33℃ 이상인 상태가 2일 이상 지속될 것으로 예상될 때
                    hw_section01 = daily_waether.iloc[list(((date_section >= start_ymd) &
                                              (date_section <= end_ymd)).index)]["최고 기온"]
                    hw_section01_eve = daily_waether.iloc[hw_section01.index - 1]["최고 기온"]

                    hw_section01.reset_index(inplace=True, drop=True)
                    hw_section01_eve.reset_index(inplace=True, drop=True)

                    # 폭염 일 수 count_heat_wave
                    count_heat_wave = pd.DataFrame([(hw_section01 >= 33.0), (hw_section01_eve >= 33.0)]).all().sum()

                    count_hw_list.append(count_heat_wave)

                    # 평균 일교차
                    daily_tp_range_list.append(daily_tp_range[list(date_section.index)])

                    # 일교차가 15 도 이상인 날 수
                    daily_tp_range_over_10.append((daily_tp_range[list(date_section.index)] > 15).sum())

                    weather_df_section.append(temp_df01.loc[list(date_section.index)])


                # 태풍
                # 작년에 파종하여 올해 수확하는 경우
                str_start_month = str(start_ymd.month)
                str_end_month = str(end_ymd.month)

                if start_ymd.month > end_ymd.month:
                    # 태풍 개수
                    typhoon_in_year = typhoon_df.loc[year-1, str_start_month:"12"].sum() + \
                                      typhoon_df.loc[year, "1":str_end_month].sum()

                    # 영향을 크게 미친 태풍 개수
                    impact_typhoon_in_year = impact_typhoon_df.loc[year-1, str_start_month:"12"].sum() + \
                                      impact_typhoon_df.loc[year, "1":str_end_month].sum()

                else:
                    # 태풍 개수
                    typhoon_in_year = typhoon_df.loc[year, str_start_month:str_end_month].sum()
                    # 영향을 크게 미친 태풍 개수
                    impact_typhoon_in_year = impact_typhoon_df.loc[year, str_start_month:str_end_month].sum()

                values_of_new_row = [sido, str_year, prod_of_sido_in_year, area_of_sido_in_year, impact_typhoon_in_year] + \
                                    [weather_section_df["일강수량"].mean()
                                     for weather_section_df in weather_df_section] + \
                                    [weather_section_df[col].mean()
                                     for weather_section_df in weather_df_section
                                     for col in col_list_of_wth] + \
                                    [tp_range.mean() for tp_range in daily_tp_range_list]+ \
                                    [tp_over for tp_over in daily_tp_range_over_10]+ \
                                    [cw for cw in count_cw_list]+ \
                                    [hw for hw in count_hw_list]

                new_row = {key: value for key, value in zip(datasets_columns, values_of_new_row)}

                final_df = pd.DataFrame.from_dict([new_row])
                # final_df = final_df.append(new_row, ignore_index=True)

                # excel 파일에 이어서 저장
                final_df.to_csv(path_to_save + crop + "_seg_dataset.csv", mode="a", header=False,
                               index=False, encoding="utf-8-sig")

#

# dataset 파일들 년도순을 정렬
def sort_dataset_by_year(dir_path):
    file_list = os.listdir(dir_path)

    for file_name in file_list:
        df = pd.read_csv(dir_path + file_name)
        df.sort_values(by=["년도", "지역"], inplace=True)
        df.to_csv(dir_path + file_name, index=False, encoding="utf-8-sig")


if __name__ == "__main__":

    scalers = ["default", "standard", "robust", "minmax"]

    set_datasets()

    sort_dataset_by_year("../datasets/종관기상관측/default/")


import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

#한글 폰트 사용
from matplotlib import font_manager, rc

datasets_path = "./종관기상관측/default/"

file_list = os.listdir(datasets_path)

# 피어슨 상관계수
temp_df = pd.read_csv(datasets_path + file_list[0])
# temp_df.drop(["지역", "년도"], axis=1, inplace=True)
# col_list = temp_df.columns

temp_df.drop(["지역", "년도", "생산량", "면적"], axis=1, inplace=True)
col_list = list(temp_df.columns) + ["면적당생산량"]

standard_correlation_coefficient = pd.DataFrame(columns=col_list)

for file in file_list:
    dataset_df = pd.read_csv(datasets_path + file)

    dataset_df.drop(["지역", "년도"], axis=1, inplace=True)

    # corr_matrix = dataset_df.corr(method='pearson')
    #
    # corr_result = corr_matrix["생산량"]

    # 면적당 생산량
    dataset_df["면적당생산량"] = dataset_df["생산량"] / dataset_df["면적"]

    dataset_df.drop(["생산량", "면적"], axis=1, inplace=True)

    corr_matrix = dataset_df.corr(method='pearson')

    if "감자_고랭지" in file:
        # drop_cols = ["풍정합", "강수량 합계", "평균 이슬점온도", "1시간 최다 일사량 평균", "일 최심적설", "10cm 지중온도",
        #              "20cm 지중온도", "30cm 지중온도", "0.5m 지중온도", "1.0m 지중온도", "1.5m 지중온도", "5.0m 지중온도",
        #              "일교차 15이상인 날", "최저 기온", "최고 기온", "최대 풍속", "최저 초상온도", "태풍 수", "최소 상대습도",
        #              "1시간 최다강수량"]
        # corr_heatmap_data = dataset_df.drop(drop_cols, axis=1).corr(method='pearson')

        corr_heatmap_data = corr_matrix

    corr_result = corr_matrix["면적당생산량"]

    index_name = file.split("_")[0] + "_" + file.split("_")[1]

    standard_correlation_coefficient.loc[index_name, :] = corr_result

print(standard_correlation_coefficient)

# 폰트 경로
font_path = "C:/Windows/Fonts/H2GTRM.TTF"
# 폰트 이름 얻어오기
font_name = font_manager.FontProperties(fname=font_path).get_name()
# font 설정
plt.rc('font', family=font_name)
# 음수 부호 설정
rc('axes', unicode_minus=False)

plt.figure(figsize=(25,25))
sns.heatmap(data=corr_heatmap_data, annot=True,
fmt='.2f', linewidths=.5, cmap='Blues')

plt.savefig("감자_고랭지_히트맵.png")

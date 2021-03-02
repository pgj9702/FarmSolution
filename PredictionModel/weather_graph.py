import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from matplotlib import font_manager

# 폰트 경로
font_path = "C:/Windows/Fonts/H2GTRM.TTF"
# 폰트 이름 얻어오기
font_name = font_manager.FontProperties(fname=font_path).get_name()
# font 설정
plt.rc('font', family=font_name)
# 음수 부호 설정
plt.rc('axes', unicode_minus=False)

df = pd.read_csv("../PreprocessingCropsData/농업주산지상세날씨/preprocessed_weather_data/배추_가을_날씨.csv")

attributes = ["일 평균상대습도", "일 평균기온", "일 평균풍속", "일 최고기온", "일 최저상대습도", "일 최저기온", "일 강수량", "일 누적일조시간"]

scatter_df = df[attributes]

scatter_df_columns = scatter_df.columns

scatter_df_indexes = list(scatter_df.index.values)

# scaler
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler()
robust_scaler = RobustScaler()

min_max_scaler.fit(scatter_df)
standard_scaler.fit(scatter_df)
robust_scaler.fit(scatter_df)

scatter_df_minmax = min_max_scaler.transform(scatter_df)
scatter_df_standard = standard_scaler.transform(scatter_df)
scatter_df_robust = robust_scaler.transform(scatter_df)

scatter_df_minmax = pd.DataFrame(scatter_df_minmax, columns=scatter_df_columns, index=scatter_df_indexes)
scatter_df_standard = pd.DataFrame(scatter_df_standard, columns=scatter_df_columns, index=scatter_df_indexes)
scatter_df_robust = pd.DataFrame(scatter_df_robust, columns=scatter_df_columns, index=scatter_df_indexes)

df[attributes] = scatter_df_robust


print(scatter_df_minmax.values[0])

for i in df.values[0]:
    print(i)

print(df)


# print(scatter_df_standard)

# scatter_matrix(scatter_df, figsize=(12, 8))
# scatter_matrix(scatter_df_minmax, figsize=(12, 8))
# scatter_matrix(scatter_df_standard, figsize=(12, 8))
# print(scatter_df_standard["일 강수량"].max(), scatter_df_standard["일 강수량"].mean(), scatter_df_standard["일 강수량"].min())
# print(df["일 강수량"].max(), df["일 강수량"].mean(), df["일 강수량"].min())

# scatter_matrix(scatter_df_robust, figsize=(12, 8))
# plt.show()

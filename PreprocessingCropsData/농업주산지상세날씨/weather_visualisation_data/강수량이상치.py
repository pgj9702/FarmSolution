from matplotlib import font_manager, rc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy

# 한글 폰트 설정
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 음수 부호 설정
rc('axes', unicode_minus=False)

gamgul_df = pd.read_csv("../preprocessed_crops_weather_data/감귤_-_날씨.csv")
jeju_df = gamgul_df[gamgul_df["지역 아이디"] == 5011000000]
print(jeju_df)

# 연월일 slicing 해서 년 column 생성
jeju_ymd = jeju_df['연월일'].str[:4].str.split('-', expand=True)  # expand = True시, dataframe 으로 만들어진다 (series->df)
jeju_ymd.columns = ["년"]
jeju_df = pd.concat([jeju_df, jeju_ymd], axis=1)
print(jeju_df)

print(gamgul_df[gamgul_df["지역 이름"] == "제주"])
print(gamgul_df[gamgul_df["지역 이름"] == "서귀포"])
print(gamgul_df.info())

#plt.rc('font', family='NanumBarunGothic')

# 강수량 data 상관관계 plot
sns.pairplot(jeju_df[['일 평균상대습도', '일 평균기온', '일 평균풍속', '일 최고기온', '일 최저상대습도',
       '일 최저기온', '일 강수량', '일 누적일조시간']])
# plt.show()
# plt.savefig("graph.png")

# python 버전 3.6.9 에서는 pandas.DataFrame.copy() 메소드 사용 안됨
data_copy = jeju_df.copy()
print(data_copy)


# 강수량 이상치
def remove_outlier_test(d_cp, column):
  fraud_column_data = d_cp[column]
  print(fraud_column_data.values)
  quan_heighest = np.percentile(fraud_column_data.values, 99.9)

  print("quan_heighest", quan_heighest)

  outlier_index = fraud_column_data[fraud_column_data > quan_heighest].index
  print(len(outlier_index))
  d_cp[column][outlier_index] = quan_heighest
  # for i in outlier_index:
    # d_cp[column][i] = 200

  # d_cp.drop(outlier_index, axis = 0, inplace=True)
  return d_cp

data_copy = remove_outlier_test(data_copy, '일 강수량')


print(data_copy[data_copy["일 강수량"] > 200])

# 이상치 제거한 값의 그래프
# jeju_df['일 강수량'] = data_copy['일 강수량']
# sns.pairplot(jeju_df[['일 평균상대습도', '일 평균기온', '일 평균풍속', '일 최고기온', '일 최저상대습도',
#                       '일 최저기온', '일 강수량', '일 누적일조시간']])
# plt.show()
# plt.savefig("graphwithoutoverfits.png")


# print("일 강수량과 일 평균상대습도 상관관계")
# print(np.corrcoef(data_copy['일 강수량'], data_copy['일 평균상대습도']))

# print("일 강수량과 일 평균기온 상관관계")
# print(np.corrcoef(data_copy['일 강수량'], data_copy['일 평균기온']))

# print("일 강수량과 일 최고기온 상관관계")
# print(np.corrcoef(data_copy['일 강수량'], data_copy['일 최고기온']))

# print("일 강수량과 일 최저상대습도 상관관계")
# print(np.corrcoef(data_copy['일 강수량'], data_copy['일 최저상대습도']))

# print("일 강수량과 일 최저기온 상관관계")
# print(np.corrcoef(data_copy['일 강수량'], data_copy['일 최저기온']))

# print("일 강수량과 일 누적일조시간 상관관계")
# print(np.corrcoef(data_copy['일 강수량'], data_copy['일 누적일조시간']))


# 지역 컬럼을 기준으로 평균값
print(pd.pivot_table(data_copy, index=["지역 이름"]))
# 특정 value 만 구해서 계산 가능 평균값
print(pd.pivot_table(data_copy, index=["지역 이름"], values=["일 최고기온"]))
# aggfunc -> mean, sum
print(pd.pivot_table(data_copy, index=["지역 이름"], values=["일 최고기온", "일 최저기온"], aggfunc=[np.mean], fill_value=0, margins=True))

# 강수량과 평균상대습도 및 기온을 확인
sns.pairplot(data_copy, x_vars=["일 강수량"], y_vars=["일 평균상대습도", "일 평균기온"], kind='reg', height=3)
plt.show()

tmp_max = data_copy["일 최고기온"].max()
print(tmp_max)
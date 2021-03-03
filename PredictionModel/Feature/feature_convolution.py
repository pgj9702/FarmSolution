from IPython.display import display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn
import platform
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge

plt.rcParams['axes.unicode_minus'] = False
path = 'c:/Windows/Fonts/malgun.ttf'

from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~~')

data = pd.read_csv("../datasets/minmax/배추_가을_dataset.csv")
print(data)

data.set_index("년도", inplace=True)
data = data.drop("지역 이름", axis=1)

area_prod_df = data.loc[:, ["면적", "생산량"]]

min_max_scaler = MinMaxScaler()
min_max_scaler.fit(area_prod_df)

print(data)

data.loc[:, ["면적", "생산량"]] = min_max_scaler.transform(area_prod_df)
# data.columns = ["feature%d" % i for i in range(10)]
# print(data.columns)
print(data)
# minmax 면적, 생산량

start_ymd = 2001
end_ymd = 2018

target = data["생산량"]

train_set = data.drop("생산량", axis=1)

X_train, X_test = train_set.loc[start_ymd:end_ymd, :], train_set.loc[end_ymd + 1:, :]

y_train, y_test = target.loc[start_ymd:end_ymd], target.loc[end_ymd + 1:]


print(X_train, X_test)
print(y_train, y_test)

score = Ridge().fit(X_train, y_train).score(X_test, y_test)
print("테스트 점수: {:.3f}".format(score))

X_train_log = np.log(X_train + 1)
X_test_log = np.log(X_test + 1)

print(X_test_log)
print(X_test_log)

score = Ridge().fit(X_train_log, y_train).score(X_test_log, y_test)
print("테스트 점수: {:.3f}".format(score))



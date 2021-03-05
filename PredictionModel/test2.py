import pandas as pd
from sklearn.preprocessing import StandardScaler
# from .preprocessing_datasets.preprocessing_datasets import preprocessing_datasets
import datetime as dt

df = pd.read_csv("../PreprocessingCropsData/농업주산지상세날씨/preprocessed_crops_weather_data/배추_가을_날씨.csv")

standard_scaler = StandardScaler()

print(df.columns)

print(df)

df = df.drop(["지역 이름", "지역 아이디", "작물 명", "작물별 특성아이디", "작물별 특성 이름", "특보 코드", "특보 발효 여부", "연월일"], axis=1)

standard_scaler.fit(df)

df_scaled = standard_scaler.fit_transform(df)

print(df_scaled)

date = dt.date(2000, 1, 1)

print(date)

date = date + dt.timedelta(days=364)
print(date)
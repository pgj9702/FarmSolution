import pandas as pd
import os

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

    corr_result = corr_matrix["면적당생산량"]

    index_name = file.split("_")[0] + "_" + file.split("_")[1]

    standard_correlation_coefficient.loc[index_name, :] = corr_result

print(standard_correlation_coefficient)

standard_correlation_coefficient.to_csv("작물별_상관계수_면적당생산량.csv")
standard_correlation_coefficient.to_excel("작물별_상관계수_면적당생산량.xlsx")

#
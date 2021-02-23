import pandas as pd

def rename_file():
    # 포도 - 캠밸
    # 양파 - 중만생종
    # 복숭아 - 유명
    # 고추 - 풋고추, 꽈리, 청양

    file_names = ["포도_캠벨얼리_날씨.csv", "양파_중만생종_날씨.csv",  "복숭아_유명_날씨.csv",
    "풋고추_꽈리고추_날씨.csv", "풋고추_청양고추_날씨.csv","풋고추_풋고추_날씨.csv"]

    new_file_names = ["포도_-_날씨.csv", "양파_-_날씨.csv", "복숭아_-_날씨.csv", "고추_-_날씨.csv"]

    path = "../preprocessed_weather_data/"

    for file, new_file in zip(file_names[:3], new_file_names[:3]):
        df = pd.read_csv(path + file)
        df.to_csv(path + new_file)

    chili_dfs = []

    for file in file_names[3:]:
        chili_dfs.append(pd.read_csv(path + file))

    chili_df = pd.concat(chili_dfs)

    chili_df.sort_values(by=["연월일"], inplace=True)

    chili_df.to_csv(path + new_file_names[3])


if __name__ == "__main__":
    rename_file()



import pandas as pd


def preprocess(area_df: pd.DataFrame, crop: str) -> pd.DataFrame:
    area_df = area_df[(area_df["항목"] == crop) & (area_df["종류별"] == "합계")]

    area_df = area_df.loc[:, columns_list]

    # 결측값은 0 으로 설정
    area_df = area_df.fillna(0)

    # '2001 년' 형식의 col 명을 '2001' 로 수정
    area_df.columns = [col.split(' ')[0] for col in area_df.columns]

    return area_df


if __name__ == "__main__":

    columns_list = ['시도별', '2001 년', '2002 년', '2003 년', '2004 년', '2005 년',
                    '2006 년', '2007 년', '2008 년', '2009 년', '2010 년', '2011 년',
                    '2012 년', '2013 년', '2014 년', '2015 년', '2016 년', '2017 년',
                    '2018 년', '2019 년', '2020 년']

    input_path = "../production_data/"
    output_path = "../preprocessed_prod_data/"

    vegetable_input_files = ["채소생산량_과채류_2001_2019.csv", "채소생산량_근채류_2001_2020.csv",
                             "채소생산량_엽채류_2001_2020.csv", "채소생산량_조미채소_2001_2020.csv"]

    vegetable_dict = {"과채류": [], "근채류": ["무_봄", "무_가을", "무_겨울", "무_고랭지", "당근", "대파"],
                      "엽채류": ["배추_봄", "배추_가을", "배추_겨울", "배추_고랭지", "시금치", "양배추"],
                      "조미채소": ["고추", "대파", "마늘", "생강", "양파", "쪽파"]}

    vegetable_output_file_list = ["무_봄_면적.csv", "무_고랭지_면적.csv", "무_가을_면적.csv", "무_겨울_면적.csv",
                                  "당근_-_면적.csv", "배추_봄_면적.csv", "배추_고랭지_면적.csv", "배추_가을_면적.csv",
                                  "배추_겨울_면적.csv", "시금치_-_면적.csv", "양배추_-_면적.csv", "고추_-_면적.csv",
                                  "마늘_-_면적.csv", "대파_-_면적.csv", "쪽파_-_면적.csv", "양파_-_면적.csv",
                                  "생강_-_면적.csv"]

    df = pd.read_csv(input_path + vegetable_input_files[1], encoding="euc-kr")

    print(df.columns)

    len_moo = [x for x in list(df.loc[0, :]) if "당근" in x]
    print(len(len_moo))

    # for crop, output_file in zip(vegetable_dict["근채류"], vegetable_output_file_list):
    #     crop_area_df = preprocess(df, crop)
    #
    #     crop_area_df.to_csv(output_path + output_file, index=False, encoding="utf-8-sig")

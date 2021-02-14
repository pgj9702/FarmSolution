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

    input_path = "../area_data/"
    output_path = "../preprocessed_area_data/"

    vegetable_input_file = "노지_채소_재배면적_2001_2020.csv"

    vegetable_list = ['봄무', '고랭지무', '가을무', '겨울무', '당근',
                      '봄배추', '고랭지배추', '가을배추', '겨울배추', '시금치',
                      '양배추', '고추', '마늘', '대파', '쪽파', '양파', '생강']

    vegetable_output_file_list = ["무_봄_면적.csv", "무_고랭지_면적.csv", "무_가을_면적.csv", "무_겨울_면적.csv",
                                  "당근_-_면적.csv", "배추_봄_면적.csv", "배추_고랭지_면적.csv", "배추_가을_면적.csv",
                                  "배추_겨울_면적.csv", "시금치_-_면적.csv", "양배추_-_면적.csv", "고추_-_면적.csv",
                                  "마늘_-_면적.csv", "대파_-_면적.csv", "쪽파_-_면적.csv", "양파_-_면적.csv",
                                  "생강_-_면적.csv"]

    df = pd.read_csv(input_path + vegetable_input_file, encoding="euc-kr")

    for crop, output_file in zip(vegetable_list, vegetable_output_file_list):
        crop_area_df = preprocess(df, crop)

        crop_area_df.to_csv(output_path + output_file, index=False, encoding="utf-8-sig")

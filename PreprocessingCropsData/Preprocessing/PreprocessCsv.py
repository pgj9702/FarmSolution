import pandas as pd


def preprocess_csv(input_file, output_file, preprocessing_func, encoding="utf-8"):

    df = pd.read_csv(input_file, encoding=encoding)

    try:
        df = preprocessing_func(df)
        df.to_csv(output_file, index=False, encoding=encoding)
    except TypeError:
        print("Error ! preprocessing_func has no return, must have return of type DataFrame")

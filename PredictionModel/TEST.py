import pandas as pd
import datetime as dt
from machine_learning.LinearRegression import reg

if __name__ == "__main__":
    train_set = pd.read_csv("datasets/감귤_-_dataset.csv")

    target = train_set["생산량"]
    
    train_set = train_set.drop(["생산량", "지역 이름"], axis=1)

    X_train, X_test = train_set.iloc[:-1, :], train_set.iloc[-1:, :]      # 년도

    y_train, y_test = target[:-1], target[-1:]

    print(X_test)

    print(X_train.shape, y_train.shape)

    linear_regression = reg(X_train, y_train)

    print("lr의 가중치(weight) : {}".format(linear_regression.coef_))
    print("lr의 편향(bias) : {}".format(linear_regression.intercept_))

    print("훈련 세트 점수 : {:.2f}".format(linear_regression.score(X_train, y_train)))

    print(y_train)

    print(linear_regression.predict(X_test))

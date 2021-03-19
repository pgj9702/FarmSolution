from sklearn.linear_model import LinearRegression

# fit_intercept : 모형에 상수항(절편)이 있는가 없는가를 결정하는 인수 (default: True)
# normalize : 매개변수 무시여부
# copy_X : X의 복사 여부
# n_jobs : 계산에 사용할 작업 수

# LinearRegression(fit_intercept, normalize, copy_X, n_jobs)
def linear_reg(X, y):

    #LinearRegression model code
    linear_reg = LinearRegression()
    linear_reg.fit(X, y)
    return linear_reg

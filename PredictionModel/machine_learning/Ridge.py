import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge

# alpha : 값이 클수록 강력한 정규화 설정하여 분산을 줄임, 양수로 설정
# fit_intercept : 모형에 상수항이 있는가 없는가를 경정하는 인수
# normalize : 매개변수 무시 여부
# copy_X : X의 복사 여부
# max_iter : 계산에 사용할 작업 수
# tol : 정밀도
# solver : 계산에 사용랑 알고리즘(auto, svd, cholesky, lsqr, sparse_cg, sag, saga)
# random_state : 난수 seed 설정

# Ridge(alpha, fit_intercept, normalize, copy_X, max_iter, tol, solver, random_state)
def ridge(X,y, alpha=10):

    ridge_01 = Ridge(alpha=alpha).fit(X,y)

    return ridge_01




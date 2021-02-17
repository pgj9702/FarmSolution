import matplotlib.pyplot as plt
import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname((__file__)))))

from ..machine_learning.Ridge import ridge
from ..machine_learning.LinearRegression import reg

def ridge_graph(linear, ridge):
    # a값에 따른 각각의 특성에 대한 가중치(coef_)의 분포도를 확인해 보자
    plt.plot(mode_lr.coef_, 'o', label='LinearRegression')
    plt.plot(ridge_01.coef_, '^', label='Ridge alpha=0.1')
    plt.plot(ridge_1.coef_, 's', label='Ridge alpha=1')
    plt.plot(ridge_10.coef_, 'v', label='Ridge alpha=10')


if __name__ == "__main__":
    ridge(X,y)
    reg(X,y)

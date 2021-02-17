import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso

# Grid Search 을 통해 규제항의 조절 파라미터 a = 0.001일 경우 좋은 성능을 나타냈다 (엽체류)
def lasso(X,y, alpha=0.001,max_iter=1000000):
    lasso_001 = Lasso(alpha=alpha, max_iter=max_iter).fit(X,y)
    return lasso_001


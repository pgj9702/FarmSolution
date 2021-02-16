from sklearn.svm import SVR


def svr(X, y, kernel="poly", gamma="auto", degree=2, C=100, epsilon=0.1):
    # 옵션 많음
    svr = SVR(kernel=kernel, gamma=gamma, degree=degree, C=C, epsilon=epsilon)
    svr.fit(X, y)
    return svr

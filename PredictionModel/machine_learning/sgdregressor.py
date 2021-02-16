from sklearn.linear_model import SGDRegressor


def sgdregressor(X, y, max_iter=100, verbose=1):
    sgd_r = SGDRegressor(max_iter=max_iter, verbose=verbose)
    sgd_r.fit(X, y)
    return sgd_r

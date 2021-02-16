from sklearn.svm import LinearSVR


def svr(X, y, epsilon=1.5, random_state=42):
    linear_svr = LinearSVR(epsilon=epsilon, random_state=random_state)
    linear_svr.fit(X, y)
    return linear_svr

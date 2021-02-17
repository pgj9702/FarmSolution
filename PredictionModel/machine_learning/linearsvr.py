from sklearn.svm import LinearSVR

# 조미 체소 -> 규제 파라미터 c = 1이 가장 좋은 성능
def svr(X, y, epsilon=1.5, random_state=42):
    linear_svr = LinearSVR(epsilon=epsilon, random_state=random_state)
    linear_svr.fit(X, y)
    return linear_svr

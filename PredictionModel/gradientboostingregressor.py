from sklearn.ensemble import GradientBoostingClassifier


def gradientboostingclassifier(X, y, random_state=42, max_depth=3, learning_rate=0.1):
    # 기본값: max_depth=3, learning_rate=0.1
    # 훈련 세트의 스코어(정확도) 가 100% 이면 overfitting, 트리의 깊이를 줄여야 함 또는 learning_rate 를 조절(0.01)
    gbc = GradientBoostingClassifier(random_state=random_state, max_depth=max_depth, learning_rate=learning_rate)
    gbc.fit(X, y)
    return gbc

from sklearn.ensemble import RandomForestClassifier

# n_estimators: random forest 에서 사용할 나무의 개수 (많아질수록 복잡도가 증가)
# max_features: 부트스트랩 샘플링에 영향을 미친다 (나무에 사용할 샘플 수)
#               -> 값이 전체 특성의 개수와 같다면 무작위성에 안들어간다 (모든 나무가 똑같은 예측)
#               -> 1이면 완전 무작위(하나의 트리에 특성이 여러개가 등록될 수도 있다)
def random_forest(X,y):
    forest = RandomForestClassifier(max_features='auto', n_estimators=5, random_state=3)
    forest.fit(X,y)
    return forest
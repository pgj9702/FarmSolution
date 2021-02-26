from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from FarmSolution.PredictionModel.datasets.get_datasets import get_train_test_datasets
import numpy as np

# n_estimators: random forest 에서 사용할 나무의 개수 (많아질수록 복잡도가 증가)
# max_features: 부트스트랩 샘플링에 영향을 미친다 (나무에 사용할 샘플 수)
#               -> 값이 전체 특성의 개수와 같다면 무작위성에 안들어간다 (모든 나무가 똑같은 예측)
#               -> 1이면 완전 무작위(하나의 트리에 특성이 여러개가 등록될 수도 있다)


def random_forest(X,y):
    forest = RandomForestClassifier(max_features='auto', n_estimators=5, random_state=3)
    forest.fit(X,y)
    return forest

#
# def grid_search_CV (X_train, y_train, X_test, y_test):
#
#     params = {'n_estimators': [10, 100],
#               'max_depth': [6, 8, 10, 12],
#               'min_samples_leaf': [8, 12, 18],
#               'min_samples_split': [8, 16, 20]
#               }
#
#     # RandomForestClassifier 객체 생성 후 GridSearchCV 수행
#     rf_clf = RandomForestClassifier(random_state=0, n_jobs=-1)
#     rf_clf.fit(X_train, y_train)
#
#     print(rf_clf.score(X_test, y_test))
#
#     grid_cv = GridSearchCV(rf_clf, param_grid=params, cv=3, n_jobs=-1)
#     grid_cv.fit(X_train, y_train)
#
#     print('최적 하이퍼 파라미터: ', grid_cv.best_params_)
#     print('최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))
#
# if __name__ == "__main__":
#
#     crop_list = ['감귤_-', '감자_가을', '감자_고랭지', '단감_-', '배추_고랭지', '복숭아_-', '사과_-', '쪽파_-', '포도_-']
#
#     df_list = []
#
#     for crop in crop_list:
#
#         path = "../datasets/"
#
#         X_train, X_test, y_train, y_test, min_max_scaler = get_train_test_datasets(path, crop, 2010, 2018)
#
#         X_test = list(X_test.iloc[0])
#         y_test = [y_test.iloc[0]]
#
#         X_test = np.array(X_test).reshape(1, -1)
#         y_test = np.array(y_test).reshape(1, -1)
#
#         print(X_train, y_train)
#
#         X_train = X_train.to_numpy()
#         # X_test = X_test.to_numpy()
#         y_train = y_train.to_numpy()
#         # y_test = y_test.to_numpy()
#
#         grid_search_CV(X_train, y_train, X_test, y_test)
#

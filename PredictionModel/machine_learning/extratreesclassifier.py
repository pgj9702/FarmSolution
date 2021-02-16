from sklearn.ensemble import ExtraTreesClassifier


def extratreeclassifier(X, y, n_estimators=5, random_state=2):
    xtree = ExtraTreesClassifier(n_estimators=n_estimators, random_state=random_state)
    xtree.fit(X, y)
    return xtree

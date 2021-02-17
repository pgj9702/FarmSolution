from sklearn.tree import DecisionTreeClassifier

def decision_tree(X,y):

    tree = DecisionTreeClassifier(random_state=0)
    tree.fit(X,y)
    return tree
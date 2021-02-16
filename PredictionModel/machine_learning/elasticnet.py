from sklearn.linear_model import ElasticNet


# 릿지, 라쏘의 절충 모델
# 제약조건에 절댓값의 합과 제곱 합이 같이 있는 회귀 모델로
# 일부의 변수와 강하게 연관되어 있을 때는 보통 엘라스틱넷(ElasticNet) 회귀를 사용한다
# l1_ratio 는 혼합 비율, 0 이면 릿지, 1이면 라쏘와 같음.
def elasticnet(X, y, alpha=0.1, l1_ratio=0.5, random_state=42):
    elastic_net = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    elastic_net.fit(X, y)
    return elastic_net

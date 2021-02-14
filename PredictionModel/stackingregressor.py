from sklearn.ensemble import StackingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import GradientBoostingRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor


def stackingregressor(X, y):
    poly_pipeline = make_pipeline(
        PolynomialFeatures(degree=2, include_bias=False),
        ElasticNet(alpha=0.1, l1_ratio=0.2)
    )
    poly_pipeline.fit(X, y)

    rfr = RandomForestRegressor()
    rfr.fit(X, y)

    gbr = GradientBoostingRegressor(random_state=42)
    gbr.fit(X, y)

    lgbm = LGBMRegressor(random_state=42)
    lgbm.fit(X, y)

    xgb = XGBRegressor(random_state=42)
    xgb.fit(X, y)

    stack_models = [
        ('elasticnet', poly_pipeline),
        ('randomforest', rfr),
        ('gbr', gbr),
        ('lgbm', lgbm),
    ]

    stack_reg = StackingRegressor(stack_models, final_estimator=xgb, n_jobs=-1)

    return stack_reg
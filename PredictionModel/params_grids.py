import numpy as np

twenty_from_zero_to_one = list(np.linspace(0.01, 1, 20))

PARAMS_GRIDS = {
    "ridge": {
        'max_iter':[10000],
        'alpha': [0.01, 0.1, 1, 2, 3, 4, 10, 30, 100, 200, 300, 400, 800, 900, 1000]
    },
    "lasso": {
        'max_iter':[10000],
        'alpha': [0.001, 0.00125, 0.0025, 0.003, 0.005, 0.01, 0.03, 0.05, 0.1, 0.25, 0.3, 0.5, 1.0, 10]
    },
    "elasticNet": {
        'max_iter': [10000],
        'l1_ratio': twenty_from_zero_to_one,
        'alpha': twenty_from_zero_to_one
    },
    "linear_svr": {
        'max_iter': [20000],
        'C': [1, 5, 10],
        'tol': [0.0001, 0.0005, 0.001],
        'intercept_scaling': [0.1, 0.5, 1],
    },
    "sgd": {
        'max_iter': [100000],
        'alpha': 10.0 ** -np.arange(1, 5),
        'loss': ['squared_loss', 'huber', 'epsilon_insensitive'],
        'penalty': ['l2', 'l1'],
        'learning_rate': ['constant', 'optimal', 'invscaling'],
    },
    "svr": {
        'max_iter': [100000],
        'kernel': ('linear', 'poly', 'rbf', 'sigmoid'),
        'C': [0.1, 1, 10, 100],
        'degree': [3, 8],
        'coef0': [0.01, 10, 0.5],
        'gamma': ('auto', 'scale')
    }
}

#[0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]



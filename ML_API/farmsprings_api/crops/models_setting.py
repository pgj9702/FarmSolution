MODELS_BY_CROP = {
    "Gamgul": {
        "model": "lasso",
        "corr": False,
        "scaler": "minmax",
        "target": "prod",
        "year": 2011,
        "seg": False,
        "params": {
            'alpha': 0.00125
        }

    },
    "PotatoFallSeg": {
        "model": "linear_svr",
        "corr": False,
        "scaler": "standard",
        "target": "prod",
        "year": 2009,
        "seg": True,
        "params": {
            'C': 5,
            'intercept_scaling': 0.1,
            'tol': 0.001
        }

    },
    "PotatoHighland": {
        "model": "ridge",
        "corr": True,
        "scaler": "minmax",
        "target": "prod",
        "year": 2012,
        "seg": False,
        "params": {
            'alpha': 0.01
        }

    },
    "PotatoSpringSeg": {
        "model": "elasticNet",
        "corr": False,
        "scaler": "standard",
        "target": "prod",
        "year": 2014,
        "seg": True,
        "params": {
            'alpha': 0.01,
            'l1_ratio': 0.5310526315789474,
        }

    },
    "Chili": {
        "model": "svr",
        "corr": True,
        "scaler": "standard",
        "target": "prod",
        "year": 2011,
        "seg": False,
        "params": {
            'C': 0.1,
            'coef0': 10,
            'degree': 3,
            'gamma': 'scale',
            'kernel': 'poly'
        }

    },
    "Dangam": {
        "model": "elasticNet",
        "corr": False,
        "scaler": "robust",
        "target": "prod",
        "year": 2016,
        "seg": False,
        "params": {
            'alpha': 0.01,
            'l1_ratio': 1.0
        }

    },
    "Carrot": {
        "model": "svr",
        "corr": True,
        "scaler": "robust",
        "target": "prod",
        "year": 2016,
        "seg": False,
        "params": {
            'C': 0.1,
            'coef0': 10,
            'degree': 3,
            'gamma': 'scale',
            'kernel': 'poly'
        }

    },
    "Largeonion": {
        "model": "svr",
        "corr": False,
        "scaler": "robust",
        "target": "prod",
        "year": 2009,
        "seg": False,
        "params": {
            'C': 1,
            'coef0': 0.5,
            'degree': 3,
            'gamma': 'auto',
            'kernel': 'poly'
        }

    },
    "PeanutSeg": {
        "model": "linear_svr",
        "corr": False,
        "scaler": "robust",
        "target": "prod",
        "year": 2010,
        "seg": True,
        "params": {
            'C': 1,
            'intercept_scaling': 0.5,
            'tol': 0.0005
        }

    },
    "GarlicSeg": {
        "model": "linear",
        "corr": False,
        "scaler": "minmax",
        "target": "prod",
        "year": 2014,
        "seg": True,
        "params": {}

    },
    "DaikonFallSeg": {
        "model": "svr",
        "corr": True,
        "scaler": "standard",
        "target": "prod",
        "year": 2015,
        "seg": True,
        "params": {
            'C': 1,
            'coef0': 0.01,
            'degree': 3,
            'gamma': 'auto',
            'kernel': 'linear'
        }

    },
    "DaikonHighlandSeg": {
        "model": "svr",
        "corr": False,
        "scaler": "standard",
        "target": "prod",
        "year": 2013,
        "seg": True,
        "params": {
            'C': 0.1,
            'coef0': 0.01,
            'degree': 3,
            'gamma': 'auto',
            'kernel': 'linear'
        }

    },
    "DaikonSpring": {
        "model": "ridge",
        "corr": False,
        "scaler": "robust",
        "target": "prod",
        "year": 2013,
        "seg": False,
        "params": {
            'alpha': 1
        }

    },
    "Pear": {
        "model": "svr",
        "corr": True,
        "scaler": "standard",
        "target": "prod",
        "year": 2014,
        "seg": False,
        "params": {
            'C': 100,
            'coef0': 0.01,
            'degree': 3,
            'gamma': 'auto',
            'kernel': 'linear'
        }

    },
    "NapacabbageFall": {
        "model": "elasticNet",
        "corr": False,
        "scaler": "robust",
        "target": "prod",
        "year": 2012,
        "seg": False,
        "params": {
            'alpha': 0.01,
            'l1_ratio': 0.4789473684210527
        }

    },
    "NapacabbageWinter": {
        "model": "lasso",
        "corr": False,
        "scaler": "robust",
        "target": "prod",
        "year": 2014,
        "seg": False,
        "params": {
            'alpha': 0.001
        }

    },
    "NapacabbageHighlandSeg": {
        "model": "linear_svr",
        "corr": False,
        "scaler": "robust",
        "target": "prod_per_area",
        "year": 2016,
        "seg": True,
        "params": {
            'C': 1,
            'intercept_scaling': 0.1,
            'tol': 0.001
        }

    },
    "NapacabbageSpringSeg": {
        "model": "svr",
        "corr": True,
        "scaler": "standard",
        "target": "prod",
        "year": 2010,
        "seg": True,
        "params": {
            'C': 100,
            'coef0': 0.01,
            'degree': 3,
            'gamma': 'auto',
            'kernel': 'linear'
        }

    },
    "PeachSeg": {
        "model": "lasso",
        "corr": True,
        "scaler": "robust",
        "target": "prod",
        "year": 2016,
        "seg": True,
        "params": {
            'alpha': 0.03
        }

    },
    "AppleSeg": {
        "model": "elasticNet",
        "corr": True,
        "scaler": "robust",
        "target": "prod",
        "year": 2015,
        "seg": True,
        "params": {
            'alpha': 0.01,
            'l1_ratio': 0.9478947368421053
        }

    },
    "Ginger": {
        "model": "sgd",
        "corr": True,
        "scaler": "minmax",
        "target": "prod",
        "year": 2012,
        "seg": False,
        "params": {
            'alpha': 0.01,
            'learning_rate': 'optimal',
            'loss': 'epsilon_insensitive',
            'penalty': 'l1'
        }

    },
    "Spinach": {
        "model": "linear_svr",
        "corr": False,
        "scaler": "minmax",
        "target": "prod",
        "year": 2015,
        "seg": False,
        "params": {
            'C': 1,
            'intercept_scaling': 0.1,
            'tol': 0.0001
        }
    },
    "Cabbage": {
        "model": "linear",
        "corr": False,
        "scaler": "minmax",
        "target": "prod",
        "year": 2016,
        "seg": False,
        "params": {}

    },
    "OnionSeg": {
        "model": "sgd",
        "corr": True,
        "scaler": "robust",
        "target": "prod",
        "year": 2009,
        "seg": True,
        "params": {
            'alpha': 0.01,
            'learning_rate': 'constant',
            'loss': 'epsilon_insensitive',
            'penalty': 'l1'
        }

    },
    "ChivesSeg": {
        "model": "ridge",
        "corr": True,
        "scaler": "standard",
        "target": "prod",
        "year": 2014,
        "seg": True,
        "params": {
            'alpha': 2
        }

    },
    "SesameSeg": {
        "model": "svr",
        "corr": False,
        "scaler": "standard",
        "target": "prod",
        "year": 2011,
        "seg": True,
        "params": {
            'C': 0.1,
            'coef0': 0.01,
            'degree': 3,
            'gamma': 'auto',
            'kernel': 'linear'
        }

    },
    "GrapeSeg": {
        "model": "sgd",
        "corr": True,
        "scaler": "robust",
        "target": "prod",
        "year": 2010,
        "seg": True,
        "params": {
            'alpha': 0.01,
            'learning_rate': 'optimal',
            'loss': 'huber',
            'penalty': 'l1'
        }

    }

}
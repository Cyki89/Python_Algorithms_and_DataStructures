''' need separate script to run multiprocesses on Windows'''

def fit_base_classifier(estimator, X_train, y_train):
    ''' fit base model in parallel '''
    
    # fit single model or pipeline
    estimator.fit(X_train, y_train)

    return estimator

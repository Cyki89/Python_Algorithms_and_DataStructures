import numpy as np
import concurrent.futures
import multiprocess_fitting

    
class AveragingClassifier():
    ''' class allows to train base models in parallel and makes them an average classifier '''
    def __init__(self, base_estimators, voting='soft'):
        self.base_estimators = base_estimators
        self.voting = voting
                 
    def fit(self, X_train, y_train, max_workers=3):
        # fitting base models in parallel
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            executor_models_holder = [executor.submit(multiprocess_fitting.fit_base_classifier, estimator, X_train, y_train) 
                                       for estimator in self.base_estimators]
            self.base_estimators = [executor_model.result() for executor_model in 
                                    concurrent.futures.as_completed(executor_models_holder)]
        return self

    def predict_proba(self, X_test):
        predicions = np.zeros( ( len(X_test), len(self.base_estimators) ) )
        for i, estimator in enumerate(self.base_estimators):
            if self.voting == 'soft':
                predicions[:,i] = estimator.predict_proba(X_test)[:,1]
            else:
                predicions[:,i] = estimator.predict(X_test) 
        return np.mean(predicions, axis=1)
                 
    def predict(self, X_test):
        return self.predict_proba(X_test).round()
import numpy as np
from sklearn.model_selection import GridSearchCV, StratifiedKFold, LeaveOneOut
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import MeanShift


class OneClassClassifier():
    '''Classifier predict one class'''
    def fit(self, X, y):
        self.cls=y[0]
    
    def predict(self, X):
        return np.array([self.cls]*len(X))
    
    
class ClusteringClassifier():
    ''' model combines clustering and classifications - 
        for each cluster choose the best classifier using GridSearchCV'''
    
    def __init__(self, clf_grid_params={'classifier': [LogisticRegression()]}, clt=MeanShift,
                 clt_params={'bandwidth':None}, n_folds=5):
        self.clt = clt(**clt_params)
        self.clf_grid_params = clf_grid_params
        self.clf_models = []
        self.n_folds=n_folds
 
    def fit(self, X, y):
        self.fit_clusterfier(X)
        # predict clusters for each sample
        clusters = self.predict_cluster(X)
        n_clusters = len(np.unique(clusters))
        # on each cluster train separate model
        for n in range(n_clusters):
            xi = X[clusters==n]
            yi = y[clusters==n]
            model = self.fit_classifier(xi, yi)
            self.clf_models.append(model)
    
    def fit_clusterfier(self, X):
        return self.clt.fit(X) 
    
    def fit_classifier(self, X, y):
        # otherwise for one class we got error
        if len(np.unique(y)) == 1:
            clf = OneClassClassifier()
            clf.fit(X, y)
        else:
            clf = self.grid_search(X, y) 
            clf.fit(X, y)  
        return clf
    
    def grid_search(self, X, y):
        kfold = StratifiedKFold(n_splits=self.n_folds, random_state=42, shuffle=True) if len(y) >= 20 else LeaveOneOut()
        pipe = Pipeline( [ ('classifier', LogisticRegression()) ] )
        grid = GridSearchCV(pipe, param_grid=self.clf_grid_params, cv=kfold, refit=True)
        grid.fit(X, y)
        return grid.best_estimator_
    
    def predict(self, X):
        # predict clusters for each data
        clusters = self.predict_cluster(X)
        n_clusters = len(np.unique(clusters))
        y_predict = np.zeros([X.shape[0]])
        # make classification using appropiate model
        for n in range(n_clusters):
            xi = X[clusters==n]
            model = self.clf_models[n]
            prediction = self.predict_class(model, xi)
            y_predict[clusters==n] = prediction
        return y_predict, clusters
            
    def predict_class(self, model, X):
        return model.predict(X) 
            
    def predict_cluster(self, X):
        return self.clt.predict(X) 
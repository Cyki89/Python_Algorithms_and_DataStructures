import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class Linear_SVC():
    ''' work well '''
    def __init__(self, C=1):
        self.C = C
        self.X = None
        self.y = None
        self.b = None
        self.w = None
    
    def fit(self, X, y):
        ''' Using 1,-1 classes '''
        self.X = X
        self.y = y

        def cost(x, *args):
            *w, b = x
            X, y = args
            return (np.linalg.norm(w)**2)/2 + self.C*np.sum(np.maximum(0,1-y*(X@w+b)))
        
        x0 = np.ones(self.X.shape[1]+1)
        params = minimize(fun=cost, x0=x0, args=(self.X, self.y))       
        *w, self.b = params['x']
        self.w = np.array(w)
        
    def predict(self, X_test):
        # sign(x.w+b)
        if self.w is None or self.b is None:
            raise Exception('Need to fit the model first!')
        return np.sign(np.dot(X_test, self.w)+self.b)
            
    def visualize(self, X_test=None):
        colors = {1: 'r', -1:'b'}
        fig = plt.figure()
        plt.title(f'C: {self.C}')
        ax = fig.add_subplot(1,1,1)
        
        if X_test is not None:
            if X_test.ndim == 1:
                X_test = X_test[np.newaxis,:]
            y_pred = self.predict(X_test)
            c = [colors[y] for y in y_pred]
            ax.scatter(X_test[:,0], X_test[:,1], s=100, marker='*', c=c)
        
        max_value = np.max([np.max([np.max(xi) for xi in self.X]), float('-inf') if X_test is None else 
                           np.max([np.max(xi) for xi in X_test])]) 
        
        min_value = np.min([np.min([np.min(xi) for xi in self.X]), float('inf') if X_test is None else 
                           np.min([np.min(xi) for xi in X_test])])
        
        [ax.scatter(xi[0], xi[1], s=50, c=colors[yi]) for xi,yi in zip(self.X, self.y)]
        
#       x,y is an unknown point on the hyperplane
#       x_v and w_v are the vector
#       x_v = [x,y]
#       x_v.w_v+b = 1 for postive sv
#       x.w[0] + y.w[1] + b =1 
#       y = -x.w[0] - b + 1 / w[1]
        def hyperplane(x, w, b, v):
            return (-w[0]*x-b+v) / w[1]
            
        datarange = (min_value*0.9, max_value*1.1)
        hyp_x_min = datarange[0]
        hyp_x_max = datarange[1]
        
        # positive support vector hyperplane (w.x+b)=1
        psv1 = hyperplane(hyp_x_min, self.w, self.b, v=1)
        psv2 = hyperplane(hyp_x_max, self.w, self.b, v=1)
        ax.plot([hyp_x_min, hyp_x_max],[psv1, psv2])
        
        # negative support vector hyperplane (w.x+b)=-1
        nsv1 = hyperplane(hyp_x_min, self.w, self.b, v=-1)
        nsv2 = hyperplane(hyp_x_max, self.w, self.b, v=-1)
        ax.plot([hyp_x_min, hyp_x_max],[nsv1, nsv2])
        
        # decision boundry  (w.x+b)=0
        db1 = hyperplane(hyp_x_min, self.w, self.b, v=0)
        db2 = hyperplane(hyp_x_max, self.w, self.b, v=0)   
        ax.plot([hyp_x_min, hyp_x_max],[db1, db2], 'k--')
        
        plt.show()

# tests
if __name__ == '__main__':

    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.datasets import make_moons

    X, y = make_moons(n_samples=100, noise=0.1, random_state=42)
    y[y==0] = -1

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1)

    for C in [1, 10, 100, 1000]:
        clf = Linear_SVC(C=C)
        clf.fit(X_train, y_train)    
        print('accuracy for train:', accuracy_score(y_train, clf.predict(X_train)))
        print('accurcy for test:', accuracy_score(y_test, clf.predict(X_test)))
        clf.visualize(X_test)
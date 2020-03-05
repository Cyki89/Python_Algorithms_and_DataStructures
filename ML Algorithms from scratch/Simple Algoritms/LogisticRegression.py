import numpy as np
from scipy.optimize import fmin_cg


class Logistic_Regression():
    def __init__(self,C=1):
        self.C = C
        self.theta = None
    
    @staticmethod
    def sigmoid(x):
        return 1/(1+np.exp(-x))
    
    def fit(self, X, y):
            
        def cost(theta, *args):
            X, y = args
            eps = 1e-20 # to avoid log(1)=0 causes division error during optimization
            m = len(y)
            lamb = 1/self.C
            return np.mean(-y*np.log(self.sigmoid(X@theta)+eps)-(1-y)*np.log(1-self.sigmoid(X@theta)+eps)) \
                   + lamb/(2*m)*sum(theta[1:]**2)

        def gradient(theta, *args):
            X, y = args
            m = len(y)
            lamb = 1/self.C   
            j_0 = 1/m * np.dot(X.T, self.sigmoid(X@theta) - y)[:1]
            j_1 = 1/m * np.dot(X.T, self.sigmoid(X@theta) - y)[1:] + (lamb/m)* theta[1:]
            grad = np.hstack((j_0,j_1))
            return grad
        
        ones = np.ones(shape=X.shape[0])
        X_ = np.column_stack((ones,X)) # add bias column 
        initial_theta = np.ones(X_.shape[1])
        
        self.theta = fmin_cg(cost, initial_theta, args=(X_, y), fprime=gradient)
    
    def predict(self, x): 
        if self.theta is None:
            raise Exception('Need to fit the model first!')
        ones = np.ones(shape=x.shape[0])
        x_ = np.column_stack((ones,x)) # add bias column 
        result = np.ones(len(x_))
        for i,xi in enumerate(x_):
            result[i] = np.round(self.sigmoid(xi@self.theta))
        return result

# tests
if __name__ == '__main__':
	
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import accuracy_score

	data = np.loadtxt('https://utkuufuk.com/2018/05/19/binary-logistic-regression/university_admission.txt', delimiter=",")
	X = data[:, 0:2]
	y = data[:, 2]
	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1)
	clf = Logistic_Regression(C=1)
	clf.fit(X_train, y_train)
	for i in range(len(y_test)):
		print('True:',y_test[i], 'Predicted:', clf.predict(X_test[i,np.newaxis])[0])
	print('Accuracy for train:', round( accuracy_score( y_train, clf.predict(X_train) ), 2) )
	print('Accuracy for test:', round( accuracy_score( y_test, clf.predict(X_test) ),2) )
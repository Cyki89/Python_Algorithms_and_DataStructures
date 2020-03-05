import numpy as np
import warnings


class LinearRegression():
	
	def __init__(self):
		self.m = None
		self.b = None
		self.R_2 = None

	def fit(self, X_train, y_train):
		if len(X_train) < 2:
			warings.warn('Model should have at leat two points')
		x_mean, y_mean = np.mean(X_train), np.mean(y_train)
		xy_mean, x2_mean = np.mean(X_train*y_train), np.mean(X_train**2)
		self.m = (x_mean * y_mean - xy_mean)/(np.square(x_mean) - x2_mean)
		self.b = y_mean - self.m*x_mean
		self.R_2 = self.score(X_train, y_train)

	def predict(self, X_test):
		if not self.m or not self.b:
			raise Exception('First need to fit the model')
		return self.m*X_test + self.b

	def score(self, X_test, y_test):	    
    		y_pred = self.predict(X_test)
    		return 1 - self.squared_error(y_test,y_pred)/self.squared_error(y_test, np.mean(y_test))

	@staticmethod
	def squared_error(y_true, y_pred):
		return np.sum((y_pred - y_true)**2)

	@staticmethod
	def create_dataset(n, var, cor = False, step=None):
		if cor and cor not in ['pos', 'neg']:
			raise TypeError('cor need to be pos or neg')
		xs = [i for i in range(n)]
		val, ys = 1, []
		for i in range(n):
			y = val + np.random.uniform(-var,var)
			ys.append(y)
			if cor and cor == 'pos':
				val += step
			elif cor and cor == 'neg':
				val -= step
		return np.array(xs), np.array(ys)

# tests
if __name__ == '__main__':
	
	from sklearn.model_selection import train_test_split
	
	X,y = LinearRegression.create_dataset(n=200, var=10, cor ='pos', step=1)
	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1)

	clf = LinearRegression()
	clf.fit(X_train, y_train)
	
	print('Test')
	print('-'*50)
	for i in range(10):
		print(f'True value: {round(y_test[i], 4)}, Predicted value: {round(clf.predict(X_test[i]), 4)}')
	print('-'*50)
	print('R^2 for train set:', round( clf.R_2, 4) )
	print('R^2 for test set:', round( clf.score(X_test, y_test), 4) )
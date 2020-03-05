import numpy as np
from collections import Counter
import warnings


class KNN():
	
	def __init__(self, k=5):
		self.k = k
		self.dataset = {}

	def fit(self, X_train, y_train):
		''' create base dataset from training data '''
		for v,k in zip(X_train, y_train):
			try:
				self.dataset[k].append(v)
			except KeyError:
				self.dataset[k] = [v]
		if len(self.dataset) >= self.k:
			warnings.warn('K should be greater then total voting groups!')
	
	def predict(self, X_test):
		''' take feture(s) and return qualified group with confidence '''
		if len(self.dataset) == 0:
			raise Exception('First need to fit the model')
		distances = []
		for group in self.dataset:
			for features in self.dataset[group]:
				euclidean_distance = np.linalg.norm(np.array(features)-np.array(X_test)) # faster way than use own function
				distances.append( (euclidean_distance, group) )
		votes = tuple( i[1] for i in sorted(distances)[:self.k] )
		counter_obj = Counter(votes).most_common(1)[0]
		vote_result = counter_obj[0]
		confidence = counter_obj[1] / self.k
		return vote_result, confidence

	def score(self, X_test, y_test):
		''' return accuracy '''
		total = len(X_test)
		correct = sum(1 for i in range(len(X_test)) if self.predict(X_test[i])[0] == y_test[i])
		return correct/total


# tests
if __name__ == '__main__':
	
	from sklearn.model_selection import train_test_split
	import pandas as pd
	
	df = pd.read_csv('breast-cancer-wisconsin.data')
	df.replace('?', -99999, inplace = True)
	df['bare_nuclei'] = df['bare_nuclei'].astype('int')
	df.drop(columns = ['id'], inplace = True)
	
	X = np.array(df.drop(columns = ['class']))
	y = np.array(df['class'])
	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

	clf = KNN(k=5)
	clf.fit(X_train, y_train)

	print('Test')
	print('-'*50)
	for i in range(10):
		print(f'True label: {y_test[i]}, Predicted label, Confidence: {clf.predict(X_test[i])}')
	print('-'*50)
	print('Test accuracy score:', round(clf.score(X_test, y_test),2))

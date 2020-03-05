import numpy as np
import warnings

class KMeansPlus():
    
    def __init__(self, n_clusters=2, init='kmeans++', n_init=10, tol=0.0001, max_iter=300):
        self.n_clusters = n_clusters
        if init not in ['kmeans++', 'random']:
            init = 'kmeans++'
            warnings.warn('init have to be kmeans++ or random, set kmeans++ as default options')
        self.init = init   
        self.n_init=n_init
        self.tol = tol
        self.max_iter = max_iter
        self.SSE = float('inf')
          
    def kmeans_random(self, X, n_clusters):
        n = X.shape[0]
        idxes = np.random.choice(a=range(n),size=n_clusters,replace=False)
        centroids = {i:X[idx] for i,idx in enumerate(idxes)}
        return centroids 
    
    def kmeans_plus(self, X, n_clusters):
        # create copy of X
        X=X.copy()
        
        # select first centroids index
        idx = np.random.choice(a=range(X.shape[0]),size=1)[0]
        centroids = {0:X[idx]}
    
        #select other centroids
        for i in range(1, n_clusters):
            # drop selected centroids from points
            X = np.concatenate([X[:idx], X[idx+1:]])
            # compute distant to closest centroid
            distances = [min(np.linalg.norm(xi-centroids[centroid]) for centroid in centroids) for xi in X]
            # create weighted probability distribution
            probability = np.array(distances)/sum(distances)
            #select and save another centroids
            idx = np.random.choice(a=range(X.shape[0]),size=1,p=probability)[0]
            centroids[i] = X[idx]
        
        return centroids
    
    def fit(self,X):
        
        if self.n_clusters > X.shape[0]:
            self.n_clusters = 2
            warnings.warn('n_clusters cannot be grater than X size, set 2 as default options')
        
        for n in range(self.n_init):
            # initial centroids cordiante
            if self.init =='random':
                centroids = self.kmeans_random(X, self.n_clusters)
            else:
                centroids = self.kmeans_plus(X, self.n_clusters)

            for i in range(self.max_iter):
                # collection to assign points to the closest centroids
                classifications = {i:[] for i in range(self.n_clusters)}

                for xi in X:
                    # compute distances to all centroids and assign point to the nearest centroid
                    distances = [np.linalg.norm(xi-centroids[centroid]) for centroid in centroids]
                    classification = distances.index(min(distances))
                    classifications[classification].append(xi) 

                prev_centroids = centroids.copy()

                # create new centroids, np.average work on list as on array
                centroids = {classification: np.average(classifications[classification], axis=0) 
                                for classification in classifications}

                # array of diffrences between centroids in current and last optimization step 
                diff = np.array([(centroids[i] - prev_centroids[i])/prev_centroids[i]
                                 for i in range(self.n_clusters)])

                # if all codrinate less the tolerance
                if np.all(diff<self.tol):
                    break

            # sum of squared errors
            SSE = sum( sum(np.linalg.norm(xi-centroids[centroid])**2 for xi in classifications[centroid] ) 
                      for centroid in centroids )

            if SSE < self.SSE:
                self.SSE = SSE
                self.centroids = centroids
                            
    def predict(self,X):
        result = []
        for x in X:
            # assign point to the nearest centroid
            distances = [np.linalg.norm(x-self.centroids[centroid]) for centroid in self.centroids]
            classification = distances.index(min(distances))
            result.append(classification)
        return np.array(result) 


# tests
if __name__ == '__main__':
    
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import datasets
    from sklearn import metrics

    iris = datasets.load_iris()
    X = iris.data  # we only take the first two features.
    y = iris.target
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.show()

    n = 11
    SSE_array = []
    for k in range(1,n):
        clt = KMeansPlus(n_clusters=k)
        clt.fit(X)
        SSE_array.append(clt.SSE)
    plt.figure(figsize=(12.5,7.5))
    plt.plot(range(1,n), SSE_array, 'o-',)
    plt.xlabel('n_clusters')
    plt.xticks(ticks=range(1,n,2))
    plt.ylabel('SSE')
    plt.show()

    km = KMeansPlus(n_clusters=3)
    km.fit(X)
    y_km = km.predict(X)
    fig, (ax1,ax2) = plt.subplots(nrows = 1, ncols = 2, figsize=(15,5))
    ax1.scatter(X[:, 0], X[:, 1], c=y_km)
    ax1.set_title('Predicted Clusters')
    ax2.scatter(X[:, 0], X[:, 1], c=y)
    ax2.set_title('Real Data')
    plt.show()
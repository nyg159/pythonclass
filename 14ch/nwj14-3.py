print("14-3.     20173087 노원진\n")

from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris  
 
iris = load_iris() 
knn = KNeighborsClassifier(n_neighbors=6) 
knn.fit(iris.data, iris.target)
classes = {0:'setosa', 1:'versicolor', 2:'virginica'} 


X = [[3,4,5,2], [5,4,2,2], [6,4,2,2] , [6,4,3,3]]
y= knn.predict(X)
print(classes[y[0]]) 
print(classes[y[1]]) 
print(classes[y[2]])
print(classes[y[3]]) 

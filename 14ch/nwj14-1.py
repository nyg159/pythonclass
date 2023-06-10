print("14-1.     20173087 노원진\n")

import numpy as np 
from sklearn import linear_model 
regr = linear_model.LinearRegression() 

X = [[164, 1],[167, 1],[165, 0],[170, 0],[179, 0],[163, 1],[159, 0],[166, 1]]             
y = [43, 48, 47, 66, 67, 50, 52, 44]     # y 값은 1차원 데이터
regr.fit(X, y)         # 학습 
print('계수 :', regr.coef_ )
print('절편 :', regr.intercept_)
print('점수 :', regr.score(X, y))
print('나의 추정 몸무게 :', regr.predict([[170, 0]]))

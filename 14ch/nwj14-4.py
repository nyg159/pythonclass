print("14-4.     20173087 노원진\n")

import numpy as np
from sklearn import linear_model

regr = linear_model.LinearRegression()
X = [[130], [250], [190], [300], [210], [220], [170]]
y=[16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2]
regr.fit(X, y)
coef = regr.coef_ 
intercept = regr.intercept_
score = regr.score(X, y)
result = regr.predict([[270]])
print("계수 :", coef)
print("절편 :", intercept)
print("예측 점수 :", score)
print('270 마력 자동차의 예상 연비 : {0:.2f}'.format(result[0]), 'km/l')
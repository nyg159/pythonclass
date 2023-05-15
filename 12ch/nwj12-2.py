print("12-2.     20173087 노원진\n")
import csv
import pandas as pd
import numpy

f = open('./data/weather.csv','rt', encoding='UTF8')
data = csv.reader(f)
header = next(data)

min_temperature = 0.0

for row in data:
    if row[1] == '':
        temperature = 100
    else :
        temperature = float(row[1])

    if min_temperature > temperature:
        min_temperature = temperature


f.close()
print('지난 10년간 울릉도의 최소 온도는 {} 도'.format(min_temperature))

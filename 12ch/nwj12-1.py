print("12-1.     20173087 노원진\n")
import csv

f = open('./data/weather.csv','rt', encoding='UTF8')
data = csv.reader(f)

row_count = 0

for row in data:
    if row_count >= 10:
        break
    row_count += 1
    print(row)

f.close()

print("7-5.  20173087 노원진\n")

x = ('A','B','C')
y = (1,2)
z =[]

x1 = list(x)
y1 = list(map(str, y))

for i in x1:
    for j in y1:
        z.append(i+j)
    
print(z)
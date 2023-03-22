n = 0

for i in range(1,10): 

        
    for j in range(2,6):
        n = i * j
        print(f"{j} * {i} = {n}", end = "\t")
    print("")

print("")

for i in range(1,10): 
    for h in range(6,10):
        n = i * h
        print(f"{h} * {i} = {n}", end = "\t")
    print("")
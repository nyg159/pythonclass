num = 0b100000
i = 0
while i < 4:
    i = i + 1
    print(num)
    num = num << 5

num = num << 5
print(num)
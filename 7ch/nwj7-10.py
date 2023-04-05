print("7-10.  20173087 노원진\n")

def overlap(a, b):
    n = len(b)

    for i in range(len(a)):  
        if a[i:] == b[:n]:
            return a + b[n:]
    
        n -= 1
         

    return a + b


while True:
    a = input("문자열1을 입력하시오. : ")
    b = input("문자열2를 입력하시오. : ")
    c = overlap(a, b)
    print(c)





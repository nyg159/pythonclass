count = 0

def fibo(n):
    global count
    count = count + 1
    if n < 0:
        print("잘못된 입력입니다.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:    
        return fibo(n - 1) + fibo(n - 2)


while True:
    i = int(input("몇 번째 항 : "))
    print(fibo(i))
    print(f"count = {count}")
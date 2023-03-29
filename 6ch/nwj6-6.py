n = 0

def fibo(n):
    count = 2
    firstTerm = 0
    secondTerm = 1
    nextTerm = 0;

    if n == 0:
        print(nextTerm)
        print(f"count = {count - 2}")
        return nextTerm
    
    if n == 1:
        nextTerm = firstTerm + secondTerm
        print(nextTerm)
        print(f"count = {count - 1}")
        return nextTerm

    while count != n:

        nextTerm = firstTerm + secondTerm
        firstTerm = secondTerm
        secondTerm = nextTerm

        count = count + 1
    
        if count == n:
            print(nextTerm)  
            print(f"count = {count - 2}")
            count = 0 
            break

    return nextTerm

    
while True:
    term = int(input("몇 번째 항 : "))
    fibo(term)

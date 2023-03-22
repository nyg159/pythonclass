smallnum = int(input("작은 정수를 입력하시오 : "))
bignum = int(input("큰 정수를 입력하시오 : "))

x = 1
for i in range(smallnum, bignum):
    x = x * i

print(f"{smallnum} 에서 {bignum} 까지를 1씩 증가시켜 가며 모두 곱한 값은 210 이다.")
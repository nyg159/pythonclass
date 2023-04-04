print("7-1.     20173087 노원진\n")
frt = []
while True:
    fruit = input("좋아하는 과일의 이름을 입력하시오. : ")
    if fruit == '없음' :
        frt.sort()
        print("오름차순 정렬: \n",frt)
        frt.reverse()
        print("내림차순 정렬: \n",frt)
        break

    frt.append(fruit)
    
        

print("8-6.     20173087 노원진\n")

fruis_dic = {
    '사과' : 0, '배' : 0, '수박' : 0, '귤' : 0, '포도' : 0 
    }

a,b,c,d,e = input('사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력 : ').split()

fruis_dic['사과'] = int(a)
fruis_dic['배'] = int(b)
fruis_dic['수박'] = int(c)
fruis_dic['귤'] = int(d)
fruis_dic['포도'] = int(e)


print("-------------- 오늘의 과일 가격 ----------------")
for key in fruis_dic.keys():
    print("{0}     :   {1} 원".format(key,fruis_dic[key]))


while True:
    fruits = input("구매를 원하는 과일의 이름을 입력하시오 : ")
    for key in fruis_dic.keys():
        if fruits == key:
            print("오늘의 {0} 가격은 {1} 원 입니다.".format(key,fruis_dic[key]))
    
    
    


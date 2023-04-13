print("8-2.     20173087 노원진\n")

items = {
    '커피음료' : 7,
    '펜' : 3,
    '종이컵' : 2,
    '우유' : 1,
    '콜라' : 4,
    '책' : 5
}

while True:
    anwser = int(input("메뉴를 선택하시오 1) 재고조회   2) 입고  3) 출고  4) 종료  : "))

    if anwser == 1:
        anwser_items = input("[재고조회] 물건의 이름을 입력하시오. : ")
        print(f"재고 : {items[anwser_items]}")

    elif anwser == 2:
        a, b = input(f"[입고] 물건의 이름과 수량을 입력하시오. : ").split()
        b = int(b)
        
        for key in items.keys():
            if key == a:
                c = items[key] + b
                items[key] = c
               
    elif anwser == 3:
        
        a, b = del_items = input(f"[출고] 물건의 이름과 수량을 입력하시오. : ").split()
        b = int(b)
        for key in items.keys():
            if key == a:
                c = items[key] - b
                if 0 >= c:
                    c = 0
                    items[key] = c
                    
                else:
                    items[key] = c
                    
    elif anwser == 4:
        print("프로그램을 종료합니다.")
        break

    else:
        print("숫자를 다시 입력 해주세요")



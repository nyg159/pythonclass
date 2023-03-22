num = 0
while True:
    words = input("단어를 입력하세요. : ")
    for ch in words:
        if ch in ['a','e','i','o','u','A','E','I','O','U']:
            num = num + 1
            continue

        print(ch,end = "")
    print("")
    print(f"단어의 모음 갯수는 {num} 개 입니다.")
        

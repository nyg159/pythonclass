print("8-3.     20173087 노원진\n")

print("사전 프로그램 시작... 종료는 q를 입력")
dictionnary = {}

while True:
    st = input('$ ')
    command = st[0]

    if command == '<':
        st = st[1:]
        inputStr = st.split(':')

        if len(inputStr) < 2:
            print("입력 오류가 발생했습니다. ")

        else:
            dictionnary[inputStr[0].strip()] = inputStr[1].strip()
    
    elif command == '>':
        st = st[1:]
        inputStr = st.strip()

        if inputStr in dictionnary:
            print(dictionnary[inputStr])
        else:
            print("{}가 사전에 없습니다.",format(inputStr))

    elif command == 'q':
        print("사전 프로그램을 종료합니다. ")
        break

    elif command == 'p':
        print(dictionnary)
    
    else:
        print('입력 오류가 발생했습니다. ')


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

# '<'로 시작하는 입력: 입력된 단어와 정의를 사전에 추가합니다. 예를 들어, <apple: a type of fruit와 같이 입력하면 'apple'이라는 단어와 정의가 사전에 추가됩니다.
# '>'로 시작하는 입력: 입력된 단어를 사전에서 검색하고 해당 단어의 정의를 출력합니다. 입력이 'apple'이라면 사전에서 'apple'에 해당하는 정의를 출력합니다.
# 'q': 프로그램을 종료합니다.
# 'p': 현재 사전의 내용을 출력합니다.
# 그 외: 입력 오류를 출력합니다.
# 위의 동작을 반복적으로 수행하며, 종료하려면 'q'를 입력하면 됩니다.

# 주어진 코드는 사용자로부터의 입력을 받아서 사전에 단어와 정의를 추가하고 검색하는 기능을 구현하였습니다. 사전은 dictionnary라는 딕셔너리로 구현되어 있습니다. 입력에 따라 각각의 동작이 수행되고, 프로그램을 종료하려면 'q'를 입력합니다.

# 주의할 점은, 코드 내에 오타가 있어서 'dictionary'를 올바르게 작성해야 합니다. ('dictionnary'가 아닌 'dictionary'로 수정)

# 출력 결과에 따라서 입력에 따른 동작을 확인할 수 있습니다.
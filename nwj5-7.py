import random

while True:
    x = random.randint(1,100)
    y = random.randint(1,100)
    print(f"{x} + {y} = ", end = "")
    answer = int(input())

    if answer == x + y:
        print("잘했어요")
    else:
        print(f"정답은 {x + y} 입니다. 다음 번에는 잘할 수 있죠?")
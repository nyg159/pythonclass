print("7-8.  20173087 노원진\n")

fruit_list=['banana', 'orange', 'kiwi', 'apple', 'melon']

max_length = max(len(fruit) for fruit in fruit_list) 
max_fruits = [fruit for fruit in fruit_list if len(fruit) == max_length] 
fruit_list = [fruit for fruit in fruit_list if len(fruit) != max_length] 
print("가장 긴 문자열 출력")
print(max_fruits)
print("리스트 출력")
print(fruit_list)


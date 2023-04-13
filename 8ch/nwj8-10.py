print("8-10.     20173087 노원진\n")

student_tuple = (('211101', '최성훈', '010-1234-4500'), ('211102', '김은지', '010-2230-6540'), 
               ('211103', '이세은', '010-3232-7788'))

student_dict = {}

for item in student_tuple:
    student_dict[item[0]] = [item[1], item[2]]
print("1. student_tuple 리스트 출력 ")
print(student_tuple)

print("\n2. (학번, 이름)의 딕셔너리 출력 ")
for key in student_dict.keys():
    print("{} : {}".format(key, student_dict[key][0]))

print("\n3. 학번으로 조회 결과 출력 ")

number = input("학번을 입력하시오. : ")

for key in student_dict.keys():
    if number == key:
        print("{} 학생은 {} 이며, 전화번호는 {} 입니다.".format(key,student_dict[key][0],student_dict[key][1]))
        
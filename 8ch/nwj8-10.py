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
        

# student_tuple 변수에 학생 정보를 튜플 형태로 저장합니다.
# student_dict 변수를 빈 딕셔너리로 초기화합니다.
# for 루프를 사용하여 student_tuple의 각 항목에 대해 반복합니다.
# item 변수는 학생 정보를 나타내는 튜플입니다.
# item[0]은 학번을 나타내며, item[1]은 이름을 나타내고, item[2]는 전화번호를 나타냅니다.
# student_dict[item[0]] = [item[1], item[2]]를 사용하여 학번을 키로 하고, 이름과 전화번호를 값으로 하는 딕셔너리 항목을 추가합니다.
# print("1. student_tuple 리스트 출력")을 사용하여 student_tuple을 출력합니다.
# print("2. (학번, 이름)의 딕셔너리 출력")을 사용하여 student_dict의 학번과 이름을 출력합니다.
# print("3. 학번으로 조회 결과 출력")을 사용하여 학번을 입력받고, 해당 학번의 이름과 전화번호를 조회하여 출력합니다.
# 이 코드는 학생 정보를 튜플 형태로 저장한 후, 딕셔너리를 활용하여 학번을 기준으로 학생 정보를 조회하는 기능을 수행합니다. 
# student_tuple을 출력하고, student_dict의 학번과 이름을 출력한 후, 학번을 입력받아 해당 학생의 이름과 전화번호를 조회하여 출력합니다. 
# 이를 통해 학생 정보를 효율적으로 관리하고 조회할 수 있습니다.
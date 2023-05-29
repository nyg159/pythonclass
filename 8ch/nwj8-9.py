print("8-9.     20173087 노원진\n")

student_tup = (('211101', '최성훈', '010-1234-4500', 4.3), ('211102', '김은지', '010-2230-6540', 3.9), 
               ('211103', '이세은', '010-3232-7788', 4.25))

student_dict = {}

for item in student_tup:
    student_dict[item[0]] = [item[1], item[2], item[3]]

num = 0
for key in student_dict.keys():
    num += student_dict[key][2]

for i in student_dict.items():
    print(i)

print("전체 학생의 학점 평균 : {:.2f}".format(num/3))

# student_tup 변수에 학생 정보를 튜플 형태로 저장합니다.
# student_dict 변수를 빈 딕셔너리로 초기화합니다.
# for 루프를 사용하여 student_tup의 각 항목에 대해 반복합니다.
# item 변수는 학생 정보를 나타내는 튜플입니다.
# item[0]은 학번을 나타내며, item[1]은 이름을 나타내고, item[2]는 전화번호를 나타내고, item[3]은 학점을 나타냅니다.
# student_dict[item[0]] = [item[1], item[2], item[3]]를 사용하여 학번을 키로 하고, 이름, 전화번호, 학점을 값으로 하는 딕셔너리 항목을 추가합니다.
# num 변수를 0으로 초기화합니다.
# for 루프를 사용하여 student_dict의 학점을 모두 더합니다.
# for 루프를 사용하여 student_dict의 항목들을 출력합니다.
# print("전체 학생의 학점 평균 : {:.2f}".format(num/3))을 사용하여 전체 학생의 학점 평균을 계산하여 출력합니다.
# 이 코드는 학생 정보를 튜플 형태로 저장한 후, 딕셔너리를 활용하여 학점 평균을 계산하는 기능을 수행합니다. 
# student_tup을 순회하면서 각 학생의 정보를 student_dict에 저장하고, 학점을 모두 더한 후 학점 평균을 계산하여 출력합니다.
# 이를 통해 학생들의 학점 정보를 관리하고 평균을 계산할 수 있습니다.
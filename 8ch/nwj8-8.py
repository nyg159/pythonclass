print("8-8.     20173087 노원진\n")

student_tup = (('211101', '최성훈', '010-1234-4500'), ('211102', '김은지', '010-2230-6540'), 
               ('211103', '이세은', '010-3232-7788'))

student_dict = {}

for item in student_tup:
    student_dict[item[0]] = [item[1], item[2]]

number = input("학번을 입력하시오. : ")

for key in student_dict.keys():
    if number == key:
        print("이름 : {}".format(student_dict[key][0]))
        print("연락처 : {}".format(student_dict[key][1]))


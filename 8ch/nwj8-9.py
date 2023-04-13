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
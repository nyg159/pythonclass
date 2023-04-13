print("8-7.     20173087 노원진\n")

student_tup = (('211101', '최성훈', '010-1234-4500'), ('211102', '김은지', '010-2230-6540'), 
               ('211103', '이세은', '010-3232-7788'))

student_dict = {}

for item in student_tup:
    student_dict[item[0]] = [item[1], item[2]]

for key in student_dict.items():
    print(key)


    

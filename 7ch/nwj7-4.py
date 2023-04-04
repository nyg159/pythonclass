print("7-4.  20173087 노원진\n")
city_info = []
city_member = ()
total_pop = 0
min_pop = 99999999999999
max_pop = 0
max_city = None
min_city = None


while True:
    a, b = input("도시명, 인구를 입력하세요. :").split()
    city_member = (a, int(b))
    if city_member == ('0', 0):
        print(city_info)
        print(f"최대인구 : {max_city[0]}, 인구 : {max_city[1]} 만명")
        print(f"최소인구 : {min_city[0]}, 인구 :  {min_city[1]} 만명")
        print(f"리스트 도시 평균 인구 : {total_pop / len(city_info)} 만명 ")
        break
    
    total_pop = total_pop + city_member[1]
    
    city_info.append(city_member)
    
    for city in city_info:
    
        if city[1] > max_pop:
            max_pop = city[1]
            max_city = city
        
        if city[1] < min_pop:
            min_pop = city[1]
            min_city = city






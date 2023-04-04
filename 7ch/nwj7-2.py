print("7-2.     20173087 노원진\n")

population  = ["sedul", 9765, "Busan", 3441, "Incheon", 2954]

print(f"서울 인구 : {population[1]}")
print(f"인천 인구 : {population[-1]}")
cities = population[0::2]
print(f"도시 리스트 : {cities}")
pops = population[1::2]
print(f"인구의 합 : {sum(pops)}")
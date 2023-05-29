print("8-4.     20173087 노원진\n")

partyA = set(['park', 'kim', 'Lee'])
partyB = set(['park', 'choi'])

print(f"파티 A, B에 참석한 사람들 : {partyA.intersection(partyB)}")
print(f"파티 A, B에 중복없이 참석한 사람 : {partyA.symmetric_difference(partyB)}")
print(f"파티 A에만 참석한 사람 : {partyA.difference(partyB)}")

# partyA와 partyB는 파티 A와 파티 B에 참석한 사람들을 나타내는 집합(set)입니다.
# partyA.intersection(partyB)는 파티 A와 파티 B에 모두 참석한 사람들의 교집합을 반환합니다.
# partyA.symmetric_difference(partyB)는 파티 A와 파티 B에 중복 없이 참석한 사람들의 집합을 반환합니다.
# partyA.difference(partyB)는 파티 A에만 참석한 사람들의 집합을 반환합니다.
# f-string을 사용하여 결과를 출력합니다.
# 따라서, 주어진 코드를 실행하면 파티 A와 파티 B에 참석한 사람들의 교집합, 중복 없이 참석한 사람들, 파티 A에만 참석한 사람들이 출력됩니다.
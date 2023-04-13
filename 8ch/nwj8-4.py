print("8-4.     20173087 노원진\n")

partyA = set(['park', 'kim', 'Lee'])
partyB = set(['park', 'choi'])

print(f"파티 A, B에 참석한 사람들 : {partyA.intersection(partyB)}")
print(f"파티 A, B에 중복없이 참석한 사람 : {partyA.symmetric_difference(partyB)}")
print(f"파티 A에만 참석한 사람 : {partyA.difference(partyB)}")


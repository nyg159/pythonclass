print("9-8.     20173087 노원진\n")

import re
s = 'Korea is awesome! I REALLY LOVE KOREA.'
s_list = re.findall('[kK][Oo][Rr][Ee][Aa]', s)
print('Korea의 출현 횟수 :', len(s_list))
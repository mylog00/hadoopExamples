# Collect all words from file

# Sample Input:
# aut Caesar aut nihil
# aut aut
# de mortuis aut bene aut nihil

# Sample Output:
# aut	6
# mortuis	1
# bene	1
# Caesar	1
# de	1
# nihil	2

import sys

map = {}

for line in sys.stdin:
    for word in line.strip().split(' '):
        val = map.get(word, 0) + 1
        map.update({word: val})
for k, v in map.items():
    print(k, v, sep='\t')

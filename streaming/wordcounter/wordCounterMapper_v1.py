# Collect all words from string

# Sample Input:
# aut Caesar aut nihil
# aut aut
# de mortuis aut bene aut nihil

# Sample Output:
# nihil	1
# aut	2
# Caesar	1
# aut	2
# nihil	1
# aut	2
# de	1
# bene	1
# mortuis	1

import sys

for line in sys.stdin:
    map = {}
    for word in line.strip().split(' '):
        val = map.get(word, 0) + 1
        map.update({word: val})
    for k, v in map.items():
        print(k, v, sep='\t')

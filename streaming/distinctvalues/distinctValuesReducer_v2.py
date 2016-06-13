# Sample Input:
# 1	a
# 1	b
# 1	b
# 2	a
# 2	d
# 2	e
# 3	a
# 3	b

# Sample Output:
# a	3
# d	1
# b	2
# e	1

import sys

map = {}
lastKey = None
lastVal = None

for line in sys.stdin:
    k, v = line.strip().split('\t')
    if lastKey == k and lastVal == v:
        continue
    else:
        val = map.get(v, 0) + 1
        map.update({v: val})
        lastKey = k
        lastVal = v
for k, v in map.items():
    print(k, v, sep='\t')

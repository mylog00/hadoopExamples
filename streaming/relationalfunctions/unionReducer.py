# see distinctValuesReducer_v1_ph1.py
# Sample Input:
# 1	A
# 2	A
# 2	B
# 3	B

# Sample Output:
# 1
# 2
# 3

import sys

lastKey = None
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    if lastKey == key:
        continue
    else:
        if lastKey:
            print(lastKey)
        lastKey = key
print(lastKey)

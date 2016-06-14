# Sample Input:
# 1	A
# 2	A
# 2	B
# 3	B
# Sample Output:
# 2

import sys

lastKey = None
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    if lastKey == key:
        print(key)
    else:
        lastKey = key

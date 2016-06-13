# Sample Input:
# 1,a	1
# 1,b	1
# 1,b	1
# 2,a	1
# 2,d	1
# 2,e	1
# 3,a	1
# 3,b	1
# Sample Output:
# 1,a
# 1,b
# 2,a
# 2,d
# 2,e
# 3,a
# 3,b

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

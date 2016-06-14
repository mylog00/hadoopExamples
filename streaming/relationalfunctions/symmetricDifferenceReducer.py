# Sample Input:
# 1	A
# 2	A
# 2	B
# 3	B

# Sample Output:
# 1
# 3

import sys

lastKey = None
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    if lastKey == key:
        lastKey = None
    else:
        if lastKey:
            print(lastKey)
        lastKey = key
if lastKey:
    print(lastKey)

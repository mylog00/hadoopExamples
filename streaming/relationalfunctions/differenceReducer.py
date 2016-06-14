# Sample Input:
# 1	A
# 2	A
# 2	B
# 3	B

# Sample Output:
# 1

import sys

lastKey = None
lastVal = None
for line in sys.stdin:
    key, val = line.strip().split('\t')
    if lastKey == key:
        lastVal = None
    else:
        if lastKey and lastVal == 'A':
            print(lastKey)
        lastKey = key
        lastVal = val
if lastKey and lastVal == 'A':
    print(lastKey)

# For reducer phase 2 user word-counter reducer

# Sample Input:
# 1,a
# 2,a
# 3,a
# 1,b
# 3,b
# 2,d
# 2,e

# Sample Output:
# a	1
# a	1
# a	1
# b	1
# b	1
# d	1
# e	1

import sys

for line in sys.stdin:
    v = line.strip().split(',')[1]
    print(v, '1', sep='\t')

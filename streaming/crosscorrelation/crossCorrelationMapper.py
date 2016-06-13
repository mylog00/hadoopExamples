# Sample Input:
# a b
# a b a c

# Sample Output:
# a,b	1
# b,a	1
# a,b	1
# a,c	1
# b,a	1
# b,a	1
# b,c	1
# a,b	1
# a,c	1
# c,a	1
# c,b	1
# c,a	1

import sys

for line in sys.stdin:
    array = line.strip().split(' ')
    for word1 in array:
        for word2 in array:
            if word1 != word2:
                print(word1 + ',' + word2, '1', sep='\t')

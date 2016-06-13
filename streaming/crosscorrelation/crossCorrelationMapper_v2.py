# Sample Input:
# a b
# a b a c

# Sample Output:
# a	b:1
# b	a:1
# a	b:1,c:1
# b	a:2,c:1
# a	b:1,c:1
# c	b:1,a:2

import sys

for line in sys.stdin:
    array = line.strip().split(' ')
    for word1 in array:
        map = {}
        for word2 in array:
            if word1 != word2:
                val = map.get(word2, 0) + 1
                map.update({word2: val})
        stripe = []
        for k, v in map.items():
            stripe.append(k + ':' + str(v))
        print(word1, ','.join(stripe), sep='\t')

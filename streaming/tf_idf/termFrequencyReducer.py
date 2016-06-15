# See wordCounterReducer.py

# Sample Input:
# aut#1	1
# aut#1	1
# aut#1	1
# aut#1	1
# aut#2	1
# aut#2	1
# bene#2	1
# de#2	1
# mortuis#2	1
# nihil#1	1
# nihil#2	1
# Caesar#1	1

# Sample Output:
# aut	1	4
# aut	2	2
# bene	2	1
# de	2	1
# mortuis	2	1
# nihil	1	1
# nihil	2	1
# Caesar	1	1

import sys

lastKey = None
counter = 0
for line in sys.stdin:
    key = line.strip().split('\t')[0]
    if lastKey == key:
        counter += 1
    else:
        if lastKey:
            word, doc = lastKey.split('#')
            print(word, doc, counter, sep='\t')
        lastKey = key
        counter = 1
word, doc = lastKey.split('#')
print(word, doc, counter, sep='\t')

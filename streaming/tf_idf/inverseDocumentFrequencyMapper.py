# Sample Input:
# aut	1	4
# aut	2	2
# bene	2	1
# de	2	1
# mortuis	2	1
# nihil	1	1
# nihil	2	1
# Caesar	1	1

# Sample Output:
# aut	1;4;1
# aut	2;2;1
# bene	2;1;1
# de	2;1;1
# mortuis	2;1;1
# nihil	1;1;1
# nihil	2;1;1
# Caesar	1;1;1

import sys

for line in sys.stdin:
    word, doc, tf = line.strip().split('\t')
    print(word, ';'.join([doc, tf, '1']), sep='\t')

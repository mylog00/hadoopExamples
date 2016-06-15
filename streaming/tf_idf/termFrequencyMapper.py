# Sample Input:
# 1:aut Caesar aut nihil
# 1:aut aut
# 2:de mortuis aut bene aut nihil

# Sample Output:
# aut#1	1
# Caesar#1	1
# aut#1	1
# nihil#1	1
# aut#1	1
# aut#1	1
# de#2	1
# mortuis#2	1
# aut#2	1
# bene#2	1
# aut#2	1
# nihil#2	1

import re
import string
import sys

regex = re.compile('[%s]' % re.escape(string.punctuation + '\t\n\r\v\f'))

for line in sys.stdin:
    docId, charsec = line.strip().split(sep=':', maxsplit=1)
    for word in regex.sub(' ', charsec).split(' '):
        if word:
            print(word + '#' + docId, '1', sep='\t')

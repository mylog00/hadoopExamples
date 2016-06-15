# Sample Input:
# aut	1;4;1
# aut	2;2;1
# bene	2;1;1
# de	2;1;1
# mortuis	2;1;1
# nihil	1;1;1
# nihil	2;1;1
# Caesar	1;1;1

# Sample Output:
# aut#1	4	2
# aut#2	2	2
# bene#2	1	1
# de#2	1	1
# mortuis#2	1	1
# nihil#1	1	2
# nihil#2	1	2
# Caesar#1	1	1

import sys

docTfList = []
lastWord = None
counter = 0
for line in sys.stdin:
    word, docTfStr = line.strip().split('\t')
    if lastWord == word:
        split = docTfStr.split(';')
        docTfList.append([split[0], split[1]])
        counter += 1
    else:
        if lastWord:
            for docTf in docTfList:
                print(lastWord + '#' + docTf[0], docTf[1], counter, sep='\t')
        lastWord = word
        counter = 1
        split = docTfStr.split(';')
        docTfList = [[split[0], split[1]]]
for docTf in docTfList:
    print(lastWord + '#' + docTf[0], docTf[1], counter, sep='\t')

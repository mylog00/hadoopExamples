import sys

lastKey = None
summ = 0
for line in sys.stdin:
    k, v = line.strip().split('\t')
    if lastKey == k:
        summ += 1
    else:
        if lastKey:
            print(lastKey, summ, sep='\t')
        lastKey = k
        summ = 1
print(lastKey, summ, sep='\t')

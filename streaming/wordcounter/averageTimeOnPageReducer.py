# Реализуйте reducer в задаче подсчета среднего времени,
# проведенного пользователем на странице.

# Sample Input:
# www.facebook.com	100
# www.google.com	10
# www.google.com	5
# www.google.com	15
# stepic.org	60
# stepic.org	100

# Sample Output:
# www.facebook.com	100
# www.google.com	10
# stepic.org	80

import sys

lastKey = None
summ = 0
counter = 1
for line in sys.stdin:
    k, v = line.strip().split('\t')
    if lastKey == k:
        summ += int(v)
        counter += 1
    else:
        if lastKey:
            print(lastKey, summ // counter, sep='\t')
        lastKey = k
        summ = int(v)
        counter = 1
print(lastKey, summ // counter, sep='\t')

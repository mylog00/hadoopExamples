# Реализуйте Reducer/Combiner в задаче подсчета среднего времени,
# проведенного пользователем на странице.

# Sample Input:
# www.facebook.com	100;1
# www.google.com	10;1
# www.google.com	5;1
# www.google.com	15;1
# stepic.org	60;1
# stepic.org	100;1

# Sample Output:
# www.facebook.com	100;1
# www.google.com	30;3
# stepic.org	160;2

import sys

lastKey = None
total = 0
counter = 1
for line in sys.stdin:
    word, value = line.strip().split('\t')
    time, num = value.split(';')
    if lastKey == word:
        total += int(time)
        counter += int(num)
    else:
        if lastKey:
            print(lastKey, str(total) + ';' + str(counter), sep='\t')
        lastKey = word
        total = int(time)
        counter = int(num)
print(lastKey, str(total) + ';' + str(counter), sep='\t')

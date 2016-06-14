# Sample Input:
# 1448713968	user2	https://ru.wikipedia.org/
# 1448764519	user10	https://stepic.org/
# 1448713968	user5	http://google.com/
# 1448773411	user10	https://stepic.org/explore/courses
# 1448709864	user3	http://vk.com/

# Sample Output:
# https://ru.wikipedia.org/
# https://stepic.org/
# http://google.com/
# https://stepic.org/explore/courses
# http://vk.com/

import sys

for line in sys.stdin:
    array = line.strip().split('\t')
    print(array[2])

# Sample Input:
# user1	query:гугл
# user1	url:google.ru
# user2	query:стэпик
# user2	query:стэпик курсы
# user2	url:stepic.org
# user2	url:stepic.org/explore/courses
# user3	query:вконтакте

# Sample Output:
# user1	гугл	google.ru
# user2	стэпик	stepic.org
# user2	стэпик	stepic.org/explore/courses
# user2	стэпик курсы	stepic.org
# user2	стэпик курсы	stepic.org/explore/courses

import sys

map = {}
lastUser = None
for line in sys.stdin:
    splitStr = line.strip().split('\t')
    user = splitStr[0]
    if user == lastUser:
        data_type, data = splitStr[1].split(':')
        array = map.get(data_type, [])
        array.append(data)
        map.update({data_type: array})
    else:
        if lastUser:
            for query in map.get('query', []):
                for url in map.get('url', []):
                    print(lastUser, query, url, sep='\t')
        map = {}
        data_type, data = splitStr[1].split(':')
        array = map.get(data_type, [])
        array.append(data)
        map.update({data_type: array})
        lastUser = user
for query in map.get('query', []):
    for url in map.get('url', []):
        print(lastUser, query, url, sep='\t')

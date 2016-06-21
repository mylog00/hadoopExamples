# Sample Input:
# 1	0	{2,3,4}
# 10	INF	{}
# 10	INF	{}
# 2	1	{}
# 2	1	{5,6}
# 3	1	{}
# 3	1	{}
# 4	1	{}
# 4	1	{7,8}
# 5	2	{}
# 5	INF	{9,10}
# 6	2	{}
# 6	INF	{}
# 7	2	{}
# 7	INF	{}
# 8	2	{}
# 8	INF	{}
# 9	INF	{}
# 9	INF	{}

# Sample Output:
# 1	0	{2,3,4}
# 10	INF	{}
# 2	1	{5,6}
# 3	1	{}
# 4	1	{7,8}
# 5	2	{9,10}
# 6	2	{}
# 7	2	{}
# 8	2	{}
# 9	INF	{}

import sys


def get_min(dist1, dist2):
    if dist1 == dist2:
        return dist1
    if dist1 == 'INF':
        return dist2
    if dist2 == 'INF':
        return dist1
    return min(dist1, dist2)


v = None
vertices = ''
min_dist = 'INF'
for line in sys.stdin:
    v_from, dist, v_to = line.strip().split('\t')
    if v == v_from:
        min_dist = get_min(dist, min_dist)
        if len(v_to) > 2:
            vertices = v_to
    else:
        if v:
            print(v, min_dist, vertices, sep='\t')
        v = v_from
        min_dist = dist
        vertices = v_to
print(v, min_dist, vertices, sep='\t')

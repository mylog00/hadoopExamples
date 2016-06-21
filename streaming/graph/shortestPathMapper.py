# Sample Input:
# 1	0	{2,3,4}
# 2	1	{5,6}
# 3	1	{}
# 4	1	{7,8}
# 5	INF	{9,10}
# 6	INF	{}
# 7	INF	{}
# 8	INF	{}
# 9	INF	{}
# 10	INF	{}

# Sample Output:
# 1	0	{2,3,4}
# 2	1	{}
# 3	1	{}
# 4	1	{}
# 2	1	{5,6}
# 5	2	{}
# 6	2	{}
# 3	1	{}
# 4	1	{7,8}
# 7	2	{}
# 8	2	{}
# 5	INF	{9,10}
# 9	INF	{}
# 10	INF	{}
# 6	INF	{}
# 7	INF	{}
# 8	INF	{}
# 9	INF	{}
# 10	INF	{}

import sys


def get_vertices(vertices_str):
    if len(vertices_str) <= 2:
        return []
    return vertices_str[1:-1].split(',')


for line in sys.stdin:
    line = line.strip()
    v_from, min_dist, vertices = line.split('\t')
    print(line)
    if min_dist != 'INF':
        min_dist = int(min_dist) + 1
    for v_to in get_vertices(vertices):
        print(v_to, min_dist, '{}', sep='\t')

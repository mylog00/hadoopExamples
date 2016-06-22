# Sample Input:
# 1	0.200	{2,4}
# 2	0.200	{3,5}
# 3	0.200	{4}
# 4	0.200	{5}
# 5	0.200	{1,2,3}

# Sample Output:
# 1	0.200	{2,4}
# 2	0.100	{}
# 4	0.100	{}
# 2	0.200	{3,5}
# 3	0.100	{}
# 5	0.100	{}
# 3	0.200	{4}
# 4	0.200	{}
# 4	0.200	{5}
# 5	0.200	{}
# 5	0.200	{1,2,3}
# 1	0.067	{}
# 2	0.067	{}
# 3	0.067	{}

import sys


def get_vertices(vertices_str):
    if len(vertices_str) <= 2:
        return []
    return vertices_str[1:-1].split(',')


for line in sys.stdin:
    line = line.strip()
    v_from, page_rank, vertices = line.split('\t')
    print(line)
    page_rank = float(page_rank)
    vertices = get_vertices(vertices)
    res_rank = '{:0.3f}'.format(page_rank / len(vertices))
    for v_to in vertices:
        print(v_to, res_rank, '{}', sep='\t')

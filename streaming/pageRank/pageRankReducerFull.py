# Calculate PageRank with respect to random transitions
# (used number of all vertices and alfa coefficient)

# Sample Input:
# 1	0.067	{}
# 1	0.200	{2,4}
# 2	0.067	{}
# 2	0.100	{}
# 2	0.200	{3,5}
# 3	0.067	{}
# 3	0.100	{}
# 3	0.200	{4}
# 4	0.100	{}
# 4	0.200	{}
# 4	0.200	{5}
# 5	0.100	{}
# 5	0.200	{}
# 5	0.200	{1,2,3}

# Sample Output:
# 1	0.080	{2,4}
# 2	0.170	{3,5}
# 3	0.170	{4}
# 4	0.290	{5}
# 5	0.290	{1,2,3}

import sys

N = 5  # vertices number
ALFA = 0.1  # page ranked coefficient

C1 = ALFA / N
C2 = 1 - ALFA


def get_rank(num):
    return '{:0.3f}'.format(C1 + C2 * num)


v = None
vertices = ''
rank_sum = 0.0
for line in sys.stdin:
    v_from, rank, v_to = line.strip().split('\t')
    rank = float(rank)
    if v == v_from:
        if len(v_to) > 2:
            vertices = v_to
        else:
            rank_sum += rank
    else:
        if v:
            print(v, get_rank(rank_sum), vertices, sep='\t')
        v = v_from
        if len(v_to) > 2:
            vertices = v_to
            rank_sum = 0.0
        else:
            rank_sum = rank
print(v, get_rank(rank_sum), vertices, sep='\t')

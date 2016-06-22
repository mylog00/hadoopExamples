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
# 1	0.067	{2,4}
# 2	0.167	{3,5}
# 3	0.167	{4}
# 4	0.300	{5}
# 5	0.300	{1,2,3}

import sys


def format_f(num):
    return '{:0.3f}'.format(num)


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
            print(v, format_f(rank_sum), vertices, sep='\t')
        v = v_from
        if len(v_to) > 2:
            vertices = v_to
            rank_sum = 0.0
        else:
            rank_sum = rank
print(v, format_f(rank_sum), vertices, sep='\t')

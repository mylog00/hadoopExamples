# Sample Input:
# 4 8
# 1 2 6
# 1 3 2
# 1 4 10
# 2 4 4
# 3 1 5
# 3 2 3
# 3 4 8
# 4 2 1
# 1 4

# Sample Output:
# 9

from heapq import heappush, heappop

import itertools


class PriorityQueue:
    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.REMOVED = '<removed-task>'  # placeholder for a removed task
        self.counter = itertools.count()  # unique sequence count

    def push(self, task, priority=0.0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return len(self.entry_finder) <= 0


class DirectedEdge:
    def __init__(self, w_from, w_to, weight=0.0):
        self.__v_from = w_from
        self.__v_to = w_to
        self.__weight = weight

    def get_from(self):
        return self.__v_from

    def get_to(self):
        return self.__v_to

    def get_weight(self):
        return self.__weight


array = input().split(' ')
vertex = int(array[0])
edge = int(array[1])
graph = []
for i in range(vertex):
    graph.append([])
i = edge
while i > 0:
    array = input().split(' ')
    v_from = int(array[0]) - 1
    v_to = int(array[1]) - 1
    weight = float(array[2])
    graph[v_from].append(DirectedEdge(v_from, v_to, weight))
    i -= 1
array = input().split(' ')
v_from = int(array[0]) - 1
v_to = int(array[1]) - 1

edgeTo = []
distTo = []
for i in range(vertex):
    edgeTo.append(None)
    distTo.append(float('inf'))

distTo[v_from] = 0
pq = PriorityQueue()
pq.push(v_from, 0)

while not pq.empty():
    next_v = pq.pop()
    for next_e in graph[next_v]:
        prev_dist = distTo[next_e.get_to()]
        next_dist = distTo[next_e.get_from()] + next_e.get_weight()
        if prev_dist > next_dist:
            distTo[next_e.get_to()] = next_dist
            edgeTo[next_e.get_to()] = next_e
            pq.push(next_e.get_to(), next_dist)

if distTo[v_to] == float('inf'):
    print('-1')
else:
    print(int(distTo[v_to]))

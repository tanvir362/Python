from queue import PriorityQueue

MAX = 99999999999

n = int(input()) #number of node
e = int(input()) #number of edge
graph = {}
weight = {}
visited = {}
distance = {}


for i in range(e):
    u, v, w = [int(x) for x in input().split()]

    weight[(u,v)] = w
    if u not in graph:
        graph[u] = []

    graph[u].append(v)

s = int(input())
distance[s] = 0
priority_queue = PriorityQueue()
priority_queue.put((distance[s], s))

print(graph)
print(weight)

# while not priority_queue.empty():
#     d, node = priority_queue.get()
#     for child in graph[node]:
#         if not visited.get(child, False):
#             if (distance.get(node, MAX) + weight.get((node, child), MAX)) < distance.get(child, MAX) :
#                 distance[child] = distance[node] + weight[(node, child)]
        
#         priority_queue.put((distance[child], child))
    
#     visited[node] = True

# print(distance)

# 6
# 8
# 1 2 2
# 1 3 4
# 2 3 1
# 2 4 7
# 3 5 3
# 5 4 2
# 5 6 5
# 4 6 1
# 1



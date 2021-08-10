n = int(input())
e = int(input())

graph = {}
vis = {}

for i in range(e):
    u, v = [int(x) for x in input().split()]
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

s = int(input())
q = [s]
vis[s] = True
print(graph)
print(q)
print(vis)
print('start traversing bfs ---------')
while len(q)>0:
    node = q.pop(0)
    print(node)
    for child in graph[node]:
        if not vis.get(child, False):
            print(child, end=" ")
            q.append(child)
            vis[child] = True
    print('\n------------')


    


# Take number of vertices and edges from user
v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Take edge input from user
edges = []
print("Enter each edge as two space-separated node numbers (e.g., 0 1):")
for _ in range(e):
    u, v_ = map(int, input().split())
    edges.append((u, v_))

# Build the adjacency list
adjlist = [[] for _ in range(v)]
for n, m in edges:
    adjlist[n].append(m)
    adjlist[m].append(n)  # Assuming undirected graph

for lst in adjlist:
    lst.sort()

# Take starting node from user
startnode=0

# BFS implementation
visited = [0] * v
ans = []
q = []

if visited[startnode] == 0:
    visited[startnode] = 1
    q.append(startnode)

    while q:
        node = q.pop(0)
        ans.append(node)
        for i in adjlist[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

print("BFS Traversal:", ans)

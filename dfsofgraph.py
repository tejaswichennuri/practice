def dfs(v, edges):
    # Build the adjacency list
    adjlist = []
    for i in range(v):
        adjlist.append([])
    for n, m in edges:
        adjlist[n].append(m)
        adjlist[m].append(n)
    for lst in adjlist:
        lst.sort()

    # DFS helper function
    def depthfirstsearch(adjlist, node, visited, ans):
        visited[node] = 1
        ans.append(node)
        for i in adjlist[node]:
            if visited[i] == 0:
                depthfirstsearch(adjlist, i, visited, ans)

    # Start DFS
    visited = [0] * v
    ans = []
    startnode = int(input("Enter starting node for DFS: "))
    if startnode < 0 or startnode >= v:
        print("Invalid starting node.")
        return []
    if visited[startnode] == 0:
        depthfirstsearch(adjlist, startnode, visited, ans)
    return ans

# Input handling
v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
edges = []
print("Enter each edge as two space-separated node numbers (e.g., 0 1):")
for _ in range(e):
    u, v_ = map(int, input().split())
    edges.append((u, v_))

# Call DFS and print result
print("DFS Traversal:", dfs(v, edges))

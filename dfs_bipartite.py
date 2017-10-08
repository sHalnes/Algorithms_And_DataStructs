
def explore(G, v):
    visited[v] = True
    global bipartite
    for u in G[v]:
        if not visited[u]:
            if (u and v in v1) or (u and v in v2):
                bipartite = False
                break
            else:
                explore(G, u)

def dfs_bipartite(G):
    for v in range(len(visited)):
        if not visited[v]:
            explore(G, v)
        if not bipartite:
            print('not bipartite')
            break
    if bipartite:
        print('Bipartite')









G = [[1,2,3], [0,2,4,6],[1], [0],[1,5],[4],[1,7,5],[6]]
visited = [False for x in range(len(G))]
v1 = [0, 2, 4, 6]
v2 = [1, 3, 7, 5]
bipartite = True
dfs_bipartite(G)



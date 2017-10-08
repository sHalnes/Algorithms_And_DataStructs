def explore(G, v):
    visited[v] = True
    print('previsit: ', v)
    for i in G[v]:
        if not visited[i]:
            explore(G, i)
    print('postvisit ', v)

def dfs(G):
    components = 0
    for v in range(len(visited)):
        if not visited[v]:
            explore(G, v)
            components += 1
    print('number of compoments: ', components)







#G = [[1, 2, 3], [0, 4, 5], [0, 5], [0, 6, 7],[1,8], [1, 2], [3, 7], [3, 6], [4], [9]]
G = [[2, 7], [0, 6], [3], [5], [0, 8], [9], [8], [5, 6], [7], [2]]
visited = [False for x in range(10)]
G_dict = {0: 'A', 1: 'B', 2: 'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}


dfs(G)
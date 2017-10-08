def graph():
    # returns an adjacensy matrix of a graph
    V = int(input('give the number of vertices'))
    print('Type inn edges:')
    L = [[] for i in range(V)] # create list
    for i in range(V):
        connections = input('Type in all connected vertices to {}, use comma as delimiter'.format(i))
        c = connections.split(',')
        for x in range(len(c)):
            L[i].append(int(c[x]))
    return L

# bread first search
def bfs(G, s):
    MAX_DIST = 1000
    distances = [MAX_DIST for x in range(len(G))]
    distances[s] = 0
    Q = []
    Q.append(s)
    while Q:
        u = Q.pop(0)
        for v in G[u]:
            if distances[v] == MAX_DIST:
                Q.append(v)
                distances[v] = distances[u] + 1
    for d in range(len(distances)):
        if d == s:
            continue
        print('the path from {} to vertex {} has length {}'.format(s, d, distances[d]))





# zero-vertex
s = 5

G = graph()
bfs(G, s)
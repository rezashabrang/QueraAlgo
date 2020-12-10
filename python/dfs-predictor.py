import sys

sys.setrecursionlimit(10 ** 9 + 100)
n, m = map(int, input().split(' '))
adj = list()
for i in range(n + 1):
    adj.append(list())
mark = (n + 1) * [False]
s, t = map(int, input().split(' '))
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def DFS(v):
    mark[v] = True
    for u in adj[v]:
        if u == t:
            return "YES"
        if not mark[u]:
            return DFS(u)
    return "NO"


print(DFS(s))

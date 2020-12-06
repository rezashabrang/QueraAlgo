q = int(input())
mod = 1e9 + 7
choices = []
ans = []
c = [[0 for i in range(2001)] for j in range(2001)]
for i in range(2001):
    for j in range(0, 2001):
        if j == 0 or j == i:
            c[i][j] = 1
        else:
            c[i][j] = int((c[i - 1][j] + c[i - 1][j - 1]) % mod)
for k in range(q):
    n, r = map(int, input().split(" "))
    ans.append(c[n][r])
for i in ans:
    print(i)

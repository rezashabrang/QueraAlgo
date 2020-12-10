matrix = []
n, q = map(int, input().split(' '))
for i in range(n):
    matrix.append(list(map(int, input().split(' '))))
qs = []
for i in range(q):
    qs.append(list(map(int, input().split(' '))))
sum_matrix = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_matrix[i][j] = matrix[i - 1][j - 1] + sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1]
for q in qs:
    x = q[0]
    y = q[1]
    X = q[2]
    Y = q[3]
    print(
        sum_matrix[X + 1][Y + 1] - sum_matrix[X + 1][y] - sum_matrix[x][Y + 1] + sum_matrix[x][y]
    )

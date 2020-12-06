# ---------------- START Processing Input
n, m = map(int, input().split(' '))
dp = [[0 for i in range(m)] for j in range(n)]
parent = [['0' for k in range(m)] for s in range(n)]
numbers = []
route = []
weight = []
for i in range(n):
    numbers.append(list(map(int, input().split(' '))))
# ---------------- END Processing Input
# ---------------- START Processing DP
dp[n - 1][0] = numbers[n - 1][0]
for i in reversed(range(n)):
    for j in range(m):
        if i == n - 1 and j == 0:
            continue
        elif j == 0:
            # first Column
            dp[i][j] = dp[i + 1][j] + numbers[i][j]
            parent[i][j] = 'down'
        elif i == n - 1:
            # final row
            dp[i][j] = dp[i][j - 1] + numbers[i][j]
            parent[i][j] = 'left'
        else:
            try:
                if dp[i + 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i + 1][j] + numbers[i][j]
                    parent[i][j] = 'down'
                else:
                    dp[i][j] = dp[i][j - 1] + numbers[i][j]
                    parent[i][j] = 'left'
            except:
                pass
# ---------------- END Processing DP
# ---------------- START Processing Route
sum_nums = []
route_dir = []
cur_row = 0
cur_col = m - 1
sum_nums.append(numbers[0][m - 1])
while (cur_row, cur_col) != (n - 1, 0):
    if parent[cur_row][cur_col] == 'down':
        cur_row += 1
        sum_nums.append(numbers[cur_row][cur_col])
        route_dir.append('U')
    else:
        cur_col -= 1
        sum_nums.append(numbers[cur_row][cur_col])
        route_dir.append('R')
# ---------------- END Processing Route
# Printing Results
print(sum(sum_nums))
for i in reversed(route_dir):
    print(i, end='')

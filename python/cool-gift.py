t, k = map(int, input().split(' '))
intervals = []
mod = 1e9 + 7
dp = [1]
for i in range(t):
    intervals.append(list(map(int, input().split(' '))))
max_len = max(map(max, intervals))
for i in range(1, max_len + 1):
    if i - k >= 0:
        dp.append((dp[i - 1] % mod + dp[i - k] % mod) % mod)
    else:
        dp.append(dp[i - 1] % mod)

ps = [dp[0]]
for indx, i in enumerate(dp[1:]):
    ps.append((ps[indx] + i) % mod)

for i in intervals:
    print(int((ps[i[1]] - ps[i[0] - 1])% mod))

import math

n = input()
n = int(n)
range_up = round(n/3)
ans = 0
for a in range(1, range_up + 1):
    ans += math.floor((n - 3 * a) / 2) - max(0, math.floor((n / 2)) - 2 * a + 1) + 1
ans %= 10**9 + 7
print(ans)

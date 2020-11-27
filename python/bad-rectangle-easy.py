ans = 0
n = input()
n = int(n)
for a in range(1, n + 1):
    for b in range(a, n - a + 1):
        c = n - a - b
        if a + b > c >= b:
            ans += 1
print(ans)

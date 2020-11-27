n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
ans = []
for i in range(-100000, 100001):
    nop = 0
    for j in range(1, len(a) + 1):
        nop += abs(i + (j - 1) * k - a[j - 1])
    ans.append(nop)

print(min(ans))

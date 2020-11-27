n = input()
n = int(n)
ans = -1e100
array_numbers = list(map(int, input().split(' ')))
max_sum = [array_numbers[0]]
for i in range(1, n):
    max_sum.append(max(array_numbers[i], array_numbers[i] + max_sum[i - 1]))
for i in range(n):
    ans = max(ans, max_sum[i])
print(ans)

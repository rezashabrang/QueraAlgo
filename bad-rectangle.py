n = input()
n = int(n)
answer = 0
for a in range(1, round(n / 3)):
    answer += round((n - 3 * a) / 2) - max(0, round(n / 2) - 2 * a + 1) + 1
answer %= 10 ** 9 + 7
print(answer)

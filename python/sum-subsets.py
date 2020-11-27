n = int(input())
a = map(int, input().split())
power_of_two = 1
mod = 10 ** 9 + 7
for i in range(1, n):
    power_of_two = (power_of_two * 2) % mod
sum_elements = 0
for x in a:
    sum_elements += x % mod
print(sum_elements * power_of_two % mod)

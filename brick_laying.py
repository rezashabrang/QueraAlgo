q = input()
questions = []
mod = 1e9 + 7
for i in range(int(q)):
    questions.append(input())
brick = [1, 1, 1, 2]
for i in range(4, int(1e5 + 1)):
    brick.append(brick[i - 1] % mod + brick[i - 2] % mod + brick[i - 3] % mod - brick[i - 4] % mod)
for i in questions:
    print(int(brick[int(i)] % mod))

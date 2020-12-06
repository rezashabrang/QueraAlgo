n, k = map(int, input().split(' '))
final = []
for i in range(k):
    numbers = list(map(int, input().split(' ')))
    for j in numbers:
        final.append(j)
for i in sorted(final):
    print(i,end=' ')
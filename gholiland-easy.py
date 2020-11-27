n, q = map(int, input().split(" "))
c = list(map(int, input().split(" ")))
d = []
for i in range(q):
    d.append(int(input()))

ans = []
for i in d:
    counter = 0
    for j in c:
        if i > j:
            counter += 1
    ans.append(counter)
for i in ans:
    print(i)

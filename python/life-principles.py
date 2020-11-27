n, m = map(int, input().split())
rule = []
h = [0]
for i in range(0, m):
    l, r, type = map(int, input().split())
    rule.append([l, r, type])
for i in range(0, len(rule) - 1):
    for j in range(i + 1, len(rule)):
        if max(rule[i][0], rule[j][0]) < min(rule[i][1], rule[j][1]) and rule[i][2] != rule[j][2]:
            print(-1)
            exit()
for i in range(2, n + 1):
    for j in range(0, m):
        if rule[j][0] < i <= rule[j][1]:
            if rule[j][2] == 0:
                h.append(h[i - 2] - 1)
                break
            else:
                h.append(h[i - 2] + 1)
                break
seq = []
for i in h:
    seq.append(i - min(h) + 1)
for i in seq:
    print(i, end=' ')

n, q = map(int, input().split(' '))
seq = list(map(int, input().split(" ")))
ps = [0 for i in range(n)]


def prep(n, seq):
    global ps
    sum = 0
    for i in range(n):
        sum += seq[i]
        ps[i] = sum


prep(n, seq)
qs = []
for i in range(q):
    l, r = map(int, input().split(' '))
    qs.append([l, r])
for q in qs:
    if q[0] == 0:
        print(ps[q[1]])
    else:
        print(ps[q[1]] - ps[q[0] - 1])

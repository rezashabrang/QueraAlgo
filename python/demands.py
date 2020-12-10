n, q = map(int, input().split(" "))
peop = []
for i in range(n):
    peop.append([i + 1])


def query1(a, b):
    global peop
    for i in peop[a - 1]:
        peop[b - 1].append(i)
    peop[a - 1] = []


def query2(c):
    if len(peop[c - 1]) == 0:
        print(0)
    else:
        print(len(peop[c - 1]))


def query3(d):
    if len(peop[d - 1]) == 0:
        print(-1)
    else:
        for i in sorted(peop[d - 1]):
            print(i, end=' ')
        print("")


qs = []
for i in range(q):
    qs.append(list(map(int, input().split(' '))))
for q in qs:
    if q[0] == 1:
        query1(q[1], q[2])
    elif q[0] == 2:
        query2(q[1])
    elif q[0] == 3:
        query3(q[1])

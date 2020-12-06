n, m = map(int, input().split(' '))
table = []
answers = []
for i in range(n):
    table.append(list(map(int, input().split(' '))))
for r1 in range(n):
    for r2 in range(r1, n):
        b = []
        for j in range(m):
            slice_table = table[r1:r2 + 1]
            slice_column = list([x[j] for x in slice_table])
            b.append(sum(slice_column))
        max_sum = [b[0]]
        for k in range(1, m):
            max_sum.append(max(b[k], b[k] + max_sum[k - 1]))
        answers.append(max(max_sum))
print(max(answers))

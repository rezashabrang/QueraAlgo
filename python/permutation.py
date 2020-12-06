number, inversions = map(int, input().split())
ans = 0


def build(n, k, current_permutation):
    global ans
    if len(current_permutation) == n:
        n_invers = 0
        for indx, i in enumerate(current_permutation):
            for nex_indx, j in enumerate(current_permutation):
                if i > j and indx < nex_indx:
                    n_invers += 1
        if n_invers == k:
            ans += 1
            return
    else:
        for i in range(1, n + 1):
            if i not in current_permutation:
                current_permutation.append(i)
                build(n, k, current_permutation)
                current_permutation.pop()


build(n=number, k=inversions, current_permutation=[])
print(ans)

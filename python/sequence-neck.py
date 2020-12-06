n = int(input())
seq = []
mark = []
for i in range(n):
    nums = list(map(int, input().split(' ')))
    seq.append(nums[1:])
    mark.append(['false' for j in range(nums[0])])
ans = 0
curr_nums = []


def find(n, current_squence, sequences):
    global ans
    global curr_nums
    global mark
    if current_squence == n:
        ans += 1
        return
    for indx, i in enumerate(sequences[current_squence]):
        if mark[current_squence][indx] == 'false'and i not in curr_nums:
            mark[current_squence][indx] = 'True'
            curr_nums.append(i)
            find(n, current_squence + 1, sequences)
            curr_nums.pop()
            mark[current_squence][indx] = 'false'



find(n=n, current_squence=0, sequences=seq)
print(ans)

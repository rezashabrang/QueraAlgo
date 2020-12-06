expr = list(input())
stack = []


def braces(expr):
    ans = []
    for indx, brace in enumerate(expr):
        if brace == '(':
            stack.append([indx, brace])
        else:
            if not stack:
                print(-1)
                return
            current_char = stack.pop()
            ans.append([current_char[0]+1, indx+1])
    if stack:
        print(-1)
    else:
        for i in ans:
            print(str(i[0])+" "+str(i[1]))


braces(expr)

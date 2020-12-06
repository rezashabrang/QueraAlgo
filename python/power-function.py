base = float(input())
exp = int(input())


def power(base, exp):
    if exp == 0:
        return 1
    result = power(base, int(exp / 2))
    if exp % 2 == 1:
        result = result * result * base
    else:
        result *= result
    return result


ans = "{0:.3f}".format(power(base, exp))
print(ans)

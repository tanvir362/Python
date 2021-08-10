n = 5
ls = [5, 1, 4, 3, 2, 1]
def duplicate_num(n, arr):
    sum1 = (n*(n+1))/2
    sum2 = 0
    for i in arr:
        sum2 += i

    return int(sum2 - sum1)

print(duplicate_num(n, ls))

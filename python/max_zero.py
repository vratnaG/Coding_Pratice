def input_take():
    N = int(input())
    arr = [int(item) for item in input().strip().split()]
    return arr, N


def seprate_num(num):
    ls = []
    while num > 0:
        ls.append(num % 10)
        num //= 10
    return ls


def count_zero(sval):
    count = 0
    for item in range(len(sval)):
        if sval[item] == 0:
            count += 1
    return count


test_case = int(input())

for case in range(test_case):
    arr, N = input_take()
    max_val = 0
    index_list = []
    f_value = 0
    for x in range(N):
        val = seprate_num(arr[x])
        out = count_zero(val)
        index_list.append(out)
        if(max_val < out):
            max_val = out
    for x in range(N):
        if(max_val == index_list[x]):
            f_value = max(f_value, arr[x])

    if(max_val == 0):
        print(-1)
    else:
        print(f_value)

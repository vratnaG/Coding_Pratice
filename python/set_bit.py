def input_take():
    N = int(input())
    return N


def count_bit(N):
    count = 0
    while N > 0:
        if(N % 2 == 1):
            count += 1
        N = N // 2
    return count


test_case = int(input())

for case in range(test_case):
    N = input_take()
    value = count_bit(N)
    print(value)

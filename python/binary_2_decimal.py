def input_take():
    N = int(input())
    return N


def count_bit(N):
    dec_val = 0
    i = 0
    while N > 0:
        dec_val += ((N % 10)*(2**i))
        i += 1
        N = N // 10
    return dec_val


test_case = int(input())

for case in range(test_case):
    N = input_take()
    value = count_bit(N)
    print(value)

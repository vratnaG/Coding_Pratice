import math


def input_take():
    N = int(input())
    return N


def power_two(N):
    pos = math.log2(N)
    return pos


test_case = int(input())

for case in range(test_case):
    N = input_take()
    if N > 0:
        out = power_two(N)
        print(out)
        print(2**out)
        if(N == 2**out and int(out) == out):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

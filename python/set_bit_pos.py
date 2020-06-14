import math

def input_take():
    N = int(input())
    return N

def position(N):
    pos=math.log2(N)
    return pos

test_case = int(input())

for case in range(test_case):
    N = input_take()
    out = position(N)
    if(N == 2**out and int(out)==out):
        print(int(out+1))
    else:
        print(-1)
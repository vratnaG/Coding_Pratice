def input_take():
    N = int(input())
    arr= [int(item) for item in input().strip().split()]
    return arr, N

def kaden(arr,N):
    maxe, maxf = 0,0
    for i in range(N):
        maxe=maxe + arr[i]
        if(maxe < 0):
            maxe=0
        if(maxf < maxe):
            maxf=maxe
    return maxf

test_case = int(input())

for case in range(test_case):
    arr, N = input_take()
    out=kaden(arr,N)
    if(out):
        print(out)
    else:
        print(arr[0])

        
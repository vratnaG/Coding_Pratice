def input_take():
    N = int(input())
    arr= [int(item) for item in input().strip().split()]
    return arr, N

test_case = int(input())

for case in range(test_case):
    arr, N = input_take()

    sum_total= sum(arr[:])
    summation= (N*(N+1))/2

    print(int(summation - sum_total))




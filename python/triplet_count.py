def input_take():
    N = int(input())
    arr= [int(item) for item in input().strip().split()]
    return arr, N

test_case = int(input())

for case in range(test_case):
    arr, N = input_take()
    count=0

    arr.sort()
    set_a = set(arr)
    max_a = arr[-1]
    
    for i in range(N-2):
        for j in range(i+1,N-1):
            s = arr[i]+arr[j]
            if(s>max_a):
                break
            elif(s in set_a):
                count+=1
    
    if count==0:
        print(-1)
    else:
        print(count)
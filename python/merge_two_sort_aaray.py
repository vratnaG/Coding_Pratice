def input_take():
    N = [int(item) for item in input().strip().split()]
    arr1= [int(item) for item in input().strip().split()]
    arr2= [int(item) for item in input().strip().split()]
    return arr1, arr2, N
def swap_value(val1,val2):
    return val1,val2
def show_value(arr1,arr2):
    for pval in range(len(arr1)):
        print(arr1[pval], end=" ")
    for pval in range(len(arr2)):
        print(arr2[pval],end=" ")

test_case = int(input())

for case in range(test_case):
    arr1,arr2, N = input_take()
    length=min(N[0],N[1])
    i,j = 0,0
    for value in range(length):
        if(arr1[i]>arr2[j]):
            arr2[j],arr1[i] = swap_value(arr1[i],arr2[j])
            if(arr2[j]>arr2[j+1]):
                arr2[j+1],arr2[j] = swap_value(arr2[j],arr2[j+1])
            i+=1
        else:
            j+=1
    for c in range(j,N[1]-1):
        if(arr2[c]>arr2[c+1]):
                arr2[c+1],arr2[c] = swap_value(arr2[c],arr2[c+1])
    show_value(arr1,arr2)
    print('')

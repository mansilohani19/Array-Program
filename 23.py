import sys


def smallest(arr):

    mini = sys.maxsize
    index = -1
    for i in range(len(arr)):
        if arr[i]<mini:
            mini = arr[i]
            index = i


    return index

def kth_smallest(arr,k):

    for i in range(k-1):
        index = smallest(arr)

        arr[index] = sys.maxsize

    
    return arr[smallest(arr)]


arr = [1,2,0,-1,3]

print(kth_smallest(arr,3))



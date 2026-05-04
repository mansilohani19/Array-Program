
def find_missing_number(arr):

    n = len(arr)

    lst = [0]*(n+1)

    for i in range(len(arr)):
        if(arr[i]<=len(arr)):
            lst[arr[i]] = 1 

    
    for i in range(1,n+1):
        if lst[i] == 0:
            return i
    
    return -1

arr = [1,3,2,5]
print(find_missing_number(arr))
def rotate_left(arr,k):
    n = len(arr)
    k = k%n

    if k == 0:
        return arr
    


    
    for i in range(len(arr)):

        arr.append(arr[i])

    length = n-k 

    ans = arr[length:length+n]

    return ans 


arr = [1,2,3,4,5]

print(rotate_left(arr,0))
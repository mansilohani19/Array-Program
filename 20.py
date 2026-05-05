def move_All_zeros_to_end(arr):
    n = len(arr)
    i = 0 
    j = i+1

    while j<n:

        if arr[i] == 0 and arr[j] != 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i+=1
            j+=1

        elif arr[i] != 0:
            i+=1
            j+=1

        else:
            j+=1

    return arr


arr = [2,3,0,4,1,0,2,0,2]
print(move_All_zeros_to_end(arr))

        

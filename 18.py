def equal_arrays(arr1,arr2):

    arr1.sort()
    arr2.sort()

    if(len(arr1) != len(arr2)):
        return False
    
    for i  in range(len(arr1)):

        if arr1[i] != arr2[i]:
            return False
        else:
            continue

    return True


arr1 = [1,2,3]
arr2=[1,3,2]

print(equal_arrays(arr1,arr2))


    
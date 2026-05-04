def intersection(arr1 , arr2):
    arr1.sort()
    arr2.sort()

    i = 0 
    j = 0 

    ans = list()

    while(i<len(arr1) and j<len(arr2)):
        if arr1[i] == arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    
    return ans 


arr1 = [1,2,3]
arr2 = [1,2,4]

print(intersection(arr1,arr2))
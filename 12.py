def merge_sorted_array(arr1 , arr2):

    s1 = 0 
    s2 = 0 

    ans = list()
    while(s1<len(arr1) and s2<len(arr2)):
        if arr1[s1]<=arr2[s2]:
            ans.append(arr1[s1])
            s1+=1
        else:
            ans.append(arr2[s2])
            s2+=1

    while(s1<len(arr1)):
        ans.append(arr1[s1])
        s1+=1

    while(s2<len(arr2)):
        ans.append(arr2[s2])
        s2+=1

    return ans


arr1 = [1,2,5]
arr2 = [3,4,6]

ans = merge_sorted_array(arr1,arr2)

print(ans)
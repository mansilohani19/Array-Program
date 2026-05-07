def find_all_subarrays(arr):

    ans = []

    for i in range(len(arr)):
        lst = []

        for j in range(i,len(arr)):
            lst.append(arr[j])
            ans.append(lst[:])

    return ans 
    

arr = [1,2,3,4]
print(find_all_subarrays(arr))

def two_sum(arr,target):
    arr.sort()
    s = 0 
    e = len(arr)-1

    while(s<e):
        if arr[s]+arr[e] == target:
            lst = [arr[s],arr[e]]
            return lst
        elif arr[s]+arr[e]<target:
            s+=1
        else:
            e-=1

    return [-1]

arr = [1,25,6,8,3,7]
target = 10 

lst = two_sum(arr,target)

print(lst)

def duplicates(arr):
    mp = dict()
    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]] +=1 
        else:
            mp[arr[i]] = 1

    lst = list()
    
    for k,v in mp.items():
        if mp[k]>1:
            lst.append(k)


    return lst 


arr = [1,1,2,4,45,2,43]
print(duplicates(arr))
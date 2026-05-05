def union(arr1,arr2):

    mp = dict()

    arr1.sort()
    arr2.sort()

    for i in range(len(arr1)):

        if arr1[i] not in mp:
            mp[arr1[i]] = 1 
        else:
            continue

    for i in range(len(arr2)):

        if arr2[i] not in mp:
            mp[arr2[i]] = 1
        else:
            continue

    lst = list()

    for k,v in mp.items():
        lst.append(k)

    return lst


arr1 = [2,3,4,1]
arr2 = [3,4,6]

print(union(arr1,arr2))


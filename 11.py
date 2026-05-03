
def remove_duplicate(arr):
    mp = dict()

    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]] = i

        else:
            continue

    lst = list()

    sorted_dict = dict(sorted(mp.items(), key=lambda x: x[1]))

    for k in mp.keys():
        lst.append(k)

    return lst 


arr = [1,2,4,2,4,6]

print(remove_duplicate(arr))
        
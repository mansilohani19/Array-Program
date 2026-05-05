def leader_elements(arr):
    lst = list()

    for i in range(len(arr)):

        num = arr[i]

        for j in range(i+1,len(arr)):

            if(arr[j]>arr[i]):
                break

        else:
            lst.append(arr[i])

    return lst 


arr = [2,3,8,4,1]
print(leader_elements(arr))

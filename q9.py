
def rotate_array(arr,k):
    k = k%len(arr)
    rotation = len(arr) - k

    lst = list()
    length = len(arr)

    for i in range(length):
        arr.append(arr[i])

    for i in range(rotation,rotation+length):
        lst.append(arr[i])

    return lst


arr = [1,2,3,4]
lst = rotate_array(arr,1)
print(lst)
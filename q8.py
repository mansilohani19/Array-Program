def is_sorted(arr):
    number = arr[0]   
    for i in range(1, len(arr)):
        if number <= arr[i]:
            number = arr[i]   
            continue
        else:
            return False

    return True
arr = [1,3,5,0]

is_sort = is_sorted(arr)
print(is_sort)
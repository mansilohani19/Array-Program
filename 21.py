def subarray_of_given_Sum(arr, target):
    ans = []

    for i in range(len(arr)):
        lst = []
        curr_sum = 0 

        for j in range(i, len(arr)):
            lst.append(arr[j])
            curr_sum += arr[j]

            if curr_sum == target:
                ans.append(lst[:])

            elif curr_sum > target:
                break

    return ans


arr = [1,2,3,4]
print(subarray_of_given_Sum(arr, 3))
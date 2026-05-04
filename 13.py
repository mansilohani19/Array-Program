
def remove_given_element(arr,target):
    if target>=len(arr):
        return ans
    
    
    

    ans = list()

    for i in range(len(arr)):
        if i != target:
            ans.append(arr[i])
        else:
            continue

    return ans 


arr = [1,23,5,2,1]
target = 2

print(remove_given_element(arr,target))

def count_freq(arr):
    mp = dict()

    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1

    return mp


arr = [1,2,3,4,1,2,4]
count = count_freq(arr)
print(count)


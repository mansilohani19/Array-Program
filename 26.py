def alternate(arr):
    arr.sort()

    n = len(arr)

    half = n//2
    small = list()
    for i in range(half):
        small.append(arr[i])

    big = list()
    for i in range(half,len(arr)):
        big.append(arr[i])

    ans = list()

    m = 0 
    o = len(big)-1
    for i in range(len(small)):

        ans.append(big[o])
        o-=1
        ans.append(small[m])
        m+=1


    return ans


arr = [1,2,3,4]
print(alternate(arr))

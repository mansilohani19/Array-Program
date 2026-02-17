def frequency(lst):

    lst.sort()
    num = lst[0]
    count = 1
    for i in range(len(lst)):

        if lst[i] != num:
            count+=1
            num = lst[i]
        
    return count 

lst = [1,2,2,2,1,1,3]
print(frequency(lst))

def reverse(lst):
    i = 0
    j = len(lst)-1

    while i<j:
        temp = lst[j]
        lst[j] = lst[i]
        lst[i] = temp
        i+=1
        j-=1

    return lst 

lst = [1,2,3,4,5]
print(reverse(lst))

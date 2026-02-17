def sum(lst):
    s = 0

    for i in lst:
        s+=i

    return s


lst = [1,2,9,0,-1]
print(sum(lst))
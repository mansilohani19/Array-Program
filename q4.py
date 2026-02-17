import sys 

inf = -10000000000
ins = sys.maxsize

def sec_largest(lst):
    maxi1 = inf
    maxi2 = inf 

    for i in lst:
        
        if maxi1<i:
            maxi1 = i

    
    for i in range(len(lst)):

        if lst[i] == maxi1:
            lst[i] = inf 

    for i in lst:

        if maxi2<i:
            maxi2 = i 

    return maxi2

lst = [1,2,9,0,11]
print(sec_largest(lst))
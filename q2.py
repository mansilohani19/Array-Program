def max_n_min(lst):

    maxi = lst[0]
    mini = lst[0]

    for i in lst:
        
        if(i>maxi):
            maxi = i 

        if(i<mini):
            mini = i 

    return maxi,mini

lst = [1,2,9,0,-1]
print(max_n_min(lst))

def is_sorted(lst):

    for i in range(len(lst)-1):
        if i+1<len(lst) and lst[i]<lst[i+1]:
            continue
        else:
            return False
        
    return True

lst = [1,2,3,4,5]
print(is_sorted(lst))
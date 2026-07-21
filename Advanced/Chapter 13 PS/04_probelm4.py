def div_by_five(n):
    if(n%5==0):
        return True
    else:
        return False
    
l=[25,50,40,22,11,43]

filter_list=list(filter(div_by_five,l))
print(filter_list)
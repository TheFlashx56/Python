from functools import reduce
#map filter 
l=[1,2,3,5,6]
square=lambda x : x*x
squared_list=map(square,l)
squared_list=list(squared_list)
print(squared_list)

#filter example
def even(n):
    if(n%2==0):
        return True
    else:
        return False

onlyEven=filter(even,l)
print(list(onlyEven))

# reduce functions 
def sum(a,b):
    return a+b

def mul(a,b):
    return a*b

print(reduce(sum,l))
print(reduce(mul,l))

"""
working of reduce function
suppose we have list l = [1,2,3,5,6]     
it will table 1,2 give to sum(1,2) -> 3
new list will be [3,3,5,6]
now it will take 3,3->sum(3,3) -> 6
new list will be [6,5,6] 
now it will take 6,5->sum(6,5) -> 11
new list be [11,6] 
it will take 11,6 in last giveme to function sum(11,6)->return 17
new list will be [17] 
now in the end sum function requirment was 2 variable and in 
list we have only 1 so it will return/give 17 as final answer
"""
from functools import reduce
def max(a,b):
    if(a>b):
        return a
    elif(b>a):
        return b
    else:
        return a 
l=[12,90,55,35,22]

max=reduce(max,l)
print(max) 
def greatest_of_three(a,b,c):
    if a>b and a>c:
            return a
    elif b>a and b>c:
            return b
    elif c>a and c>b:
            return c       
    
    
a=int(input("Enter number 1: "))  
b=int(input("Enter number 2: "))  
c=int(input("Enter number 3: "))   

greatest=greatest_of_three(a,b,c)

print(f"{greatest} is greatest number")
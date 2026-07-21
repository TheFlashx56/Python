a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if(b==0):
    raise ZeroDivisionError('Division of any number with zero is not allowed')
else:
    print(f"div={a/b}")

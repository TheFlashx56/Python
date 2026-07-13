n1 = int(input("Enter a number 1 : "))
n2 = int(input("Enter a number 2 : "))
n3 = int(input("Enter a number 3 : "))
n4 = int(input("Enter a number 4 : "))


if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print(f"{n1} is largest number ")
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    print(f"{n2} is largest number ")
elif n3 >= n1 and n3 >= n2 and n3 >= n4:
    print(f"{n3} is largest number ")
elif n4 >= n1 and n4 >= n2 and n4 >= n3:
    print(f"{n4} is largest number ")

else:
    print("All number are equal")

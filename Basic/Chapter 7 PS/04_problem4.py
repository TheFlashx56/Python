number=int(input("Enter a Number : "))

for i in range(2,number):
    if(number%i==0):
        print(f"{number} is not Prime ")
        break

else :
        print(f"{number} is a  Prime number ")
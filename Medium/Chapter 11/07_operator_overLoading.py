class Number:
    def __init__(self,a):
        self.a=a
        
    def __add__(self,num):
        return self.a+num.a

n=Number(1)

m=Number(2)


print(n+m)
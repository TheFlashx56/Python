class Demo:
    a=4


o=Demo()
print(o.a)
o.a=0 ## this Lines does not change class aTTribute
print(o.a) 
Demo.a=9 # This Line is surely changing class Attribute
b=Demo()
print(b.a)
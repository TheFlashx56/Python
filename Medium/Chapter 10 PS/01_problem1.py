class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode

    def display(self):
        print(f"--------------------{self.company}------------------")
        print("Employee Details")
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"PinCode : {self.pincode}") 



employee1=Programmer('Mubashir',200000,7200)
employee1.display()

employee2=Programmer('eass',220000,7220)
employee2.display()
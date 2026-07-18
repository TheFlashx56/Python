class emp:
    name="Mubashir"
    language="urdu"
    salary=12000
    def getInfo(self):
        print(f"{self.name},{self.language},{self.salary}")
    
    def __init__(self,name,salary,language):
        self.name=name  
        self.salary=salary
        self.language=language
     
    def display(self):
        print(f"Name : {self.name}")
        print(f"Language : {self.language}")
        print(f"Salary : {self.salary}")  
    @staticmethod    
    def greet():
        print("Good Morning")
    
    

name=input("Enter Employ Name : ")
salary=int(input("Enter Employ Salary : "))
language=input("Enter Employe Specialization Language : ")
emp1=emp(name,salary,language)
emp1.greet()
emp1.display()
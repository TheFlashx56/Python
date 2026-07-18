class emp:
    name="Mubashir"
    language="urdu"
    salary=12000
    def getInfo(self):
        print(f"{self.name},{self.language},{self.salary}")
      
    @staticmethod    
    def greet():
        print("Good Morning")
    
    
p2=emp()
p2.greet()
p2.name="Eass"
p2.language="Math"
p2.salary=1000000000
print(f"Name : {p2.name}")
print(f"Language : {p2.language}")
print(f"salary : {p2.salary}")

p1=emp()
p1.getInfo()


class Employee:
    salary=234
    increament=20
    @property
    def salary_after_increament(self):
        return self.salary+(self.salary*(self.increament/100))
    @salary_after_increament.setter
    def salary_after_increament(self,salary):
        self.increament=((salary/self.salary-1)*100)
        

e=Employee() 
e.salary_after_increament=280
print(e.increament)
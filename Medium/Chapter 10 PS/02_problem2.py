class Calculator:
    def __init__(self,number):
        self.number=number
    
    def getSquare(self):
        print(f"The Square is {self.number*self.number}")
        
    def Cube(self):
        print(f"The Cube is {self.number**3}")
        
    def squareRoot(self):
        print(f"The Square Root is {self.number**1/2}")
       
 
a=Calculator(4)
a.getSquare()    
a.Cube()
a.squareRoot()   
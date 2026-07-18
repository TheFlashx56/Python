class two_D_vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"{self.i}i + {self.j}j")

class three_D_vector(two_D_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k   
    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k") 

a=two_D_vector(10,90)        
b=three_D_vector(11,91,220)
a.show()
b.show()

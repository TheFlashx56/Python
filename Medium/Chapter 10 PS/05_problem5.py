from random import randint

class Train:
    
    def __init__(self,name,StationCity,DestinationCity):
        self.name=name
        self.TicketNumber=randint(0,100001)
        self.StationCity=StationCity
        self.DestinationCity=DestinationCity
        self.SeatNumber=randint(1,201)
        self.fare=randint(200,1000)
    def printTicket(self):
        print(f"Name: {self.name}")
        print(f"Seat Number : {self.SeatNumber}")
        print(f"Ticket Number : {self.TicketNumber}")
        print(f"Current City : {self.StationCity}")
        print(f"Destination City : {self.DestinationCity}")
        
        print(f"--------------------TOTAL FARE IS: ${self.fare}-----------------")
       

p1=Train('Mubashir',"dadu","Larkana")
p1.printTicket()
        
from random import randint

class Train:
    
    def __init__(slf,name,StationCity,DestinationCity):
        slf.name=name
        slf.TicketNumber=randint(0,100001)
        slf.StationCity=StationCity
        slf.DestinationCity=DestinationCity
        slf.SeatNumber=randint(1,201)
        slf.fare=randint(200,1000)
    def printTicket(self):
        print(f"Name: {self.name}")
        print(f"Seat Number : {self.SeatNumber}")
        print(f"Ticket Number : {self.TicketNumber}")
        print(f"Current City : {self.StationCity}")
        print(f"Destination City : {self.DestinationCity}")
        
        print(f"--------------------TOTAL FARE IS: ${self.fare}-----------------")
       

p1=Train('Mubashir',"dadu","Larkana")
p1.printTicket()
        
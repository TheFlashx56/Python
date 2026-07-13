p1 = "Make  a lot of money "
p2 = "Buy Now"
p3 = "Subscribe this"
p4 = "Click this"
messege = input("Enter your comment : ")
if p1 in messege or p2 in messege or p3 in messege or p4 in messege:
    print("SPAM MESSEGE DETECTED")
else:
    print(messege)

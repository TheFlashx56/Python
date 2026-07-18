
with open("this.txt",'r')  as f:
    copy=f.read()
    
with open("copy.txt",'w') as f:
    f.write(copy)
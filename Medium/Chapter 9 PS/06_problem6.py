with  open("log.txt",'r') as f:
    file=f.read()
    

if("python" in file):
    print("Yes python is present ")
else:
    print("No Python is not present")
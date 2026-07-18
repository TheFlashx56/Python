with  open("log.txt",'r') as f:
    lines=f.readlines()
    
linesno=1
for line in lines:
    if("python" in line):
        print(f"Yes python is present in line no: {linesno} ")
        break
    linesno+=1
else:
    print("No Python is not present")
    
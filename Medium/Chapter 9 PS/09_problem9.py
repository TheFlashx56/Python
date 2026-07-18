
with open("this.txt",'r')  as f:
    file1=f.read()
    
with open("copy.txt",'r') as f:
    file2=f.read()

if(file2==file1):
    print("Content Matches IDENTITCAL Files")
else:
    print("Content Does not Matches ")
words=["Fuck","Bitch","Bad"]
with open("file.txt",'r') as f:
    content=f.read()


for i in words:
    content=content.replace(i,"#####")

with open("file.txt",'w') as f:
    f.write(content)
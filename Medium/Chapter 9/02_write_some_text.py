string="Hey Mubashir You are Amazing"

f=open("file2.txt","w") 
f.write(string)

f=open("file2.txt")
data=f.read()
print(f"Text :\"{data}\" has been Written in file2.txt")

f.close()
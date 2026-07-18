f=open("poem.txt")
c=f.read()
if("twinkle" in c):
        print("We Found Twinkle in peom.txt")
else:
        print("error 404. Twinkle NOt found in poem.txt")
    
f.close()
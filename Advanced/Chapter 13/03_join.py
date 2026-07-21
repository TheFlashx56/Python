a=['mubashir','eass','tayyab',"Preetam"]


i=0
while(i<len(a)):
    a[i]=a[i].capitalize()
    i+=1
final=" :: ".join(a)

print(final)
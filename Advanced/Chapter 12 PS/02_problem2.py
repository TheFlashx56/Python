l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(l)):
#     if(i%2!=0):
#         print(i)
#     else:
#         continue

i = 1
while i < len(l):
    if l[i] % 2 != 0:
        print(l[i])
        i += 1
    else:
        i += 1
        continue

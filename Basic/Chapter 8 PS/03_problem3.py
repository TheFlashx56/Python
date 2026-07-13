def first_n(n):
    if n==1:
        return 1
    else:
      return first_n(n-1)+n
    
   
print(first_n(5))  
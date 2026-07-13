def f_c(fer):
    return 5*(fer-32)/9

F=int(input("ENter temperature in F : "))
print(f"{round(f_c(F),2)} C")
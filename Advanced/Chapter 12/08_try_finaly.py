def main():
    try:
        a=int(input("Enter a numer "))
        print(a)
        return 

    except Exception as e:
        print(e)
        return

  
    finally:
        print("i am in finally")
    
main()   
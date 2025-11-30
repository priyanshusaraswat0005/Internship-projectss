while True:
    try:
       a=int(input("Enter number:"))
       if a>0:
        print("Its a Positive Number...")
       elif a==0:
        print("Its a Zero...")
       else:
        print("Its a Negetive Number...")
    except:
        print("Enter Only Integer...")
        break
    
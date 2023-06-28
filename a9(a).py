try:
    a=input("Enter 1st number:")
    b=input("Enter 2nd number:")
    if(a.isdigit() and b.isdigit()):
        print("Result of sum is:",int(a)+int(b))
    else:
        raise Exception
except:
    print("Non number value is taken!")

import math as m
try:
    r=eval(input("Enter number:"))
    s=m.sqrt(r)
    print("Result of root is:",s)
except:
    print("Negative number entered")
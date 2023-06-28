def sumofsquare(m):
    if(m<0):
        return False
    else:
        for i in range(1,m):
            k=i**2
            for j in range(1,m):
                l=j**2
                if(m==k+l):
                    return True
        return False

n=int(input("Enter number:"))
if(sumofsquare(n)):
    print("True")
else:
    print("False")

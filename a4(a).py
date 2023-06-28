x=int(input("Enter the x value of x^n = "))
n=int(input("Enter the n value of x^n = "))
#with while loop
k=n
y=1
while(n>0):
	y=y*x
	n=n-1
print("y =",y)
#with for loop
Y=1
for i in range(k):
	Y=Y*x
print("y =",Y)
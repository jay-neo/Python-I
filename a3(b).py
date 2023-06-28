import math
from cmath import sqrt
a=float(input("Enter the coefficient of x^2 = "))
b=float(input("Enter the coefficient of x = "))
c=float(input("Enter the constant value = "))
D=b*b-4*a*c
if(a!=0):
	if(D>0):
		r1=(-b+math.sqrt(D))/(2*a)
		r2=(-b-math.sqrt(D))/(2*a)
		print("Roots are real, not equal",r1,"and",r2)
	elif(D<0):
		r1=(-b+sqrt(D))/(2*a)
		r2=(-b-sqrt(D))/(2*a)
		print("Roots are imaginary",r1,"and",r2)
	else:
		r=(-b)/(2*a)
		print("Roots are real, equal",r)
else:
	print("This is not quadratic equation.")

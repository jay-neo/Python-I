a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if(a>b and a>c):
	print("Maximum =",a)
elif(b>a and b>c):
	print("Maximum =",b)
else:
	print("Maximum =",c)
'''
if(a>b and a>c):
	print("Maximum =",a)
	if(b>c):
		print("Maximum =",b)
	else:
		print("Maximum =",c)

'''

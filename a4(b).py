n=int(input("Enter the number of terms = "))
print("Fibonacci Seires is:")
a=0
b=1
result=0
if n<=0:
	print("Invalid input.")
elif n==1:
	print(a)
else:
	print(a)
	print(b)
	for i in range(n-2):
		result=a+b
		a=b
		b=result
		print(result)
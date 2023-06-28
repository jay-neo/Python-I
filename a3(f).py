unit=float(input("Enter the consumption unit = "))

if(unit>=0 and unit<=200):
	bill=unit*0.50
	print("The bill is",bill)
elif(unit>200 and unit<=400):
	bill=100+(unit-200)*0.65
	print("The bill is",bill)
elif(unit>400 and unit<=600):
	bill=200+(unit-400)*0.80
	print("The bill is",bill)
elif(unit>600):
	bill=300+(unit-600)
	print("The bill is",bill)
else:
	print("Invalid Input!")
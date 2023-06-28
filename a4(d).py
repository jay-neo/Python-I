num=int(input("Enter the number = "))
temp=num
rev=0
while temp>0:
	l=len(str(temp))
	rem=temp%10
	rev+=rem*10**(l-1)
	temp//=10
print("Reverse number is ",rev)
if num==rev:
	print("It is a palindrome number.")
else:
	print("It is not a palindrome number.")

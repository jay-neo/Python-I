s=int(input("Enter your choice = "))
n=int(input("Enter the number of rows = "))
if s==1:
	for i in range(n):
		for j in range(n):
			if i==j or i+j==n-1:
				print(" $ ",end="")
			elif (i==0 or j==0 or i==n-1 or j==n-1):
				print(" * ",end="")
			else:
				print("   ",end="")
		print("")
elif s==2:
	for i in range(n,0,-1):
		ch="A"
		for j in range(i):
			print(ch,end="")
			x=ord(ch)+1
			ch=chr(x)
		if i==n:
			val=ord(ch)-2
		else:
			val=ord(ch)-1
			for j in range(2*(n-i-1)+1):
				print(" ",end="")
		while val>64:
			ch=chr(val)
			print(ch,end="")
			val-=1
		print("")


elif s==3:
	for i in range(1,n+1):
		for j in range(n,i,-1):
			print(" ",end="")
		for k in range(1,i+1):
			print(k,end="")
		print("")
else:
	print("Invalid input!")
a=11
b=100
for i in range(a,b+1):
	n=i
	temp=10
	sqr=i*i
	while i>0:
		if n==sqr%temp:
			print(n)
			break
		i=i//10
		temp=temp*10

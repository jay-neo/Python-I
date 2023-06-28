a=100
b=999
for i in range(a,b+1):
	temp=i
	result=0
	while temp>0:
		r=1
		rem=temp%10
		for j in range(1,rem+1):
			r=r*j
		result=result+r
		temp=temp//10
	if result==i:
		print(i)

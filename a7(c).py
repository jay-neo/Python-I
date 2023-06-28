a=input()
b=a.split(',')
n=len(b)
for i in range(n-1):
	for j in range(n-i-1):
		if(b[j]>b[j+1]):
			temp=b[j]
			b[j]=b[j+1]
			b[j+1]=temp


c=''
for item in b:
	c=c+item+','
c=c[:len(c)-1]
print(c)

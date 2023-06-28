strr=input()
u=0
l=0
for item in strr:
	if item.isupper():
		u+=1
	elif item.islower():
		l+=1
print(u,l)
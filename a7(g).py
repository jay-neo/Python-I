def middle(s1,s2):
	L=len(s1)
	l=L//2
	s3=s1[0:l]+s2+s1[l:]
	return s3
p=input("Enter the orginal string: ")
q=input("Enter the middle string to insert: ")
print(middle(p,q))
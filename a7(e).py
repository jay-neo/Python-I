def wellbracketed(s):
	r=0
	l=0
	for item in s:
		if s=='(':
			l+=1
		elif s==')':
			r+=1
	if l==r:
		return True
	else:
		return False
strr=input()
print(wellbracketed(strr))

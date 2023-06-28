def rotatelist(l,k):
	n=len(l)
	if k<1:
		k=0
	for i in range(k):
		l.insert(0,l[n-1])
		l.pop(n)
	return l

n=int(input("Enter the size of array = "))
arr=[]
print("Enter the elements of array:")
for i in range(n):
	arr.append(int(input()))
shift=int(input("Enter the number of rotation = "))
arr=rotatelist(arr,shift)
print(arr)

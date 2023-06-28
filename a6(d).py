import numpy as np
print("1.Linear Search\n2.Binary Search")
s=int(input("Enter your choice = "))
n=int(input("Enter the size of array = "))
print("Enter",n,"elements of array:")
arr=np.zeros(n,dtype=int)
for item in range(n):
	arr[item]=int(input())
key=int(input("Enter the key value to find = "))
print("Given array:")
print(arr)

if s==1:
	f=1
	for i in range(n):
		if key==arr[i]:
			print(key,"value is found in",i+1,"th position of given array.")
			f=0
	if f:
		print("Not found in given array!")

elif s==2:
	f=1
	for i in range(n-1):
		for j in range(n-i-1):
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
	l=0
	r=n-1
	while l<=r:
		mid=(l+r)//2
		if key<arr[mid]:
			r=mid-1
		elif key>arr[mid]:
			l=mid+1
		else:
			print(arr)
			print(key,"value is found in",mid+1,"th position of sorted array.")
			f=0
			break
	if f:
		print("Not found in given array!")

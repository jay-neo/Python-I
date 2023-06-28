import numpy as np
print("1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort")
s=int(input("Enter your choise = "))
n=int(input("Enter the size of array = "))
arr=np.zeros(n,dtype=int)
for item in range(n):
	arr[item]=int(input())
print("Before sorting the array is:")
print(arr)
if s==1:
	for i in range(n-1):
		for j in range(n-i-1):
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
elif s==2:
	for i in range(n-1):
		for j in range(i+1,n):
			if(arr[j]<arr[i]):
				arr[j],arr[i]=arr[i],arr[j]
elif s==3:
	for i in range(1,n):
		temp=arr[i]
		j=i-1
		while(arr[j]>temp and j>=0):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=temp
print("After sorting:")
print(arr)
import numpy as np
print("Press 1 for 1D array\nPress 2 for 2D array")
s=int(input("Enter your choice = "))
if s==1:
	n=int(input("Enter the size of 1D array = "))
	print("Enter",n,"elements of array:")
	arr=np.zeros(n,dtype=int)
	for item in range(n):
		arr[item]=int(input())
	s_num=arr[0]
	for i in range(n):
		if s_num>arr[i]:
			s_num=arr[i]
	l_num=arr[0]
	for i in range(n):
		if l_num<arr[i]:
			l_num=arr[i]
	print(arr)
	print("Largest in 1D array =",l_num)
	print("Samllest in 1D array =",s_num)

if s==2:
	row=int(input("Enter the row size of 2D array = "))
	col=int(input("Enter the columns size of 2D array = "))
	print("Enter",row*col,"elements of array:")
	arr=np.zeros((row,col),dtype=int)
	for r in range(row):
		for c in range(col):
			arr[r][c]=int(input())
	s_num=arr[0][0]
	for i in range(row):
		for j in range(col):
			if s_num>arr[i][j]:
				s_num=arr[i][j]
	l_num=arr[0][0]
	for i in range(row):
		for j in range(col):
			if l_num<arr[i][j]:
				l_num=arr[i][j]
	print(arr)
	print("Largest in 2D array =",l_num)
	print("Samllest in 2D array =",s_num)


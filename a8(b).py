def snake_mat(M):
	result=[]
	for i in range(row):
		for j in range(col):
			if (i+1)%2==0:
				result.append(M[i][col-j-1])
			else:
				result.append(M[i][j])
	print(result)

print("Enter the size of row of first matrix = ")
row=int(input())
print("Enter the size of cloumn of first matrix = ")
col=int(input())


M=[]
print("For",row,"x",col,"Matrix")
for i in range(row):
	M.append([])
for i in range(row):
	for j in range(col):
		M[i].append(j)
		M[i][j]=0
for i in range(row):
	for j in range(col):
		print("Enter the element of ",i+1,"th row",j+1,"th column")
		M[i][j]=int(input())

print(M)
snake_mat(M)
def matmult(M1,M2):
	Matrix=[]
	for i in range(row):
		Matrix.append([])
	for i in range(row):
		for j in range(row):
			Matrix[i].append(j)
			Matrix[i][j]=0
	for i in range(row):
		for j in range(row):
			for k in range(col):
				Matrix[i][j]+=M1[i][k]*M2[k][j]
	print(Matrix)


print("Enter the size of row of first matrix = ")
row=int(input())
print("Enter the size of column of first matrix = ")
col=int(input())


M1=[]
print("For First",row,"x",col,"Matrix")
for i in range(row):
	M1.append([])
for i in range(row):
	for j in range(col):
		M1[i].append(j)
		M1[i][j]=0
for i in range(row):
	for j in range(col):
		print("Enter the element of ",i+1,"th row",j+1,"th column")
		M1[i][j]=int(input())


M2=[]
print("For Second",col,"x",row,"Matrix")
for i in range(col):
	M2.append([])
for i in range(col):
	for j in range(row):
		M2[i].append(j)
		M2[i][j]=0
for i in range(col):
	for j in range(row):
		print("Enter the element of ",i+1,"th row",j+1,"th column")
		M2[i][j]=int(input())

print(M1)
print(M2)
matmult(M1,M2)
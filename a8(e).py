arr=[]
dic={}
n=int(input("Enter the size = "))
for i in range(n):
	arr.append(int(input()))
for i in range(n):
	temp_arr=[]
	curr=arr[i]
	if curr not in dic:
		for j in range(n):
			if(curr==arr[j]):
				temp_arr.append(j)
		if(len(temp_arr)>=2):
			dic[curr]=temp_arr
print(dic)
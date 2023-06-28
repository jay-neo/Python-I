n=int(input("Enter the size of list = "))
print("Enter the",n,"elements of list")
my_list=[]
for i in range(n):
	my_list.append(int(input()));
new_list=[]
for ele in my_list:
	if ele>0:
		new_list.append(ele)
new_list=tuple(new_list)
print(new_list)
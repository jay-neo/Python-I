import numpy as np

p=6
print("Enter the",p,"elements of array P")
arr_P=np.zeros(p,dtype=int)
for i in range(p):
	arr_P[i]=int(input())
arr_P=np.sort(arr_P)

q=4
print("Enter the",q,"elements of array P")
arr_Q=np.zeros(q,dtype=int)
for i in range(q):
	arr_Q[i]=int(input())
arr_Q=np.sort(arr_Q)

arr_R=np.concatenate((arr_P,arr_Q))
arr_R=np.sort(arr_R)
print(arr_P)
print(arr_Q)
print(arr_R)
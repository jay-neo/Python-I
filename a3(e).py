total_class=int(input("Enter the number of class held = "))
attended_class=int(input("Enter the number of class ateneded = "))

percentage=(attended_class/total_class)*100
print("Percenage of class attended =",percentage,"%")
if(percentage>=75):
	print("This student is allowed to give exam.")
else:
	med=input("Enter Y/N for medical cause = ")
	if(med=='Y' or med=='y'):
		print("This student is allowed to give exam for medical cause.")
	elif(med=='N' or med=='n'):
		print("This student is not allowed to give exam.")
	else:
		print("Invalid input")

class Demo:
	def __init__(self):
		self.str1=''
	def Get_String(self):
		self.str1=input("Enter the your string = ")
	def Print_String(self):
		print((self.str1).upper())

obj=Demo()
obj.Get_String()
obj.Print_String()
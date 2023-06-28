class Point:
	x=0
	y=0
	def Display(self):
		print("X =",self.x)
		print("Y =",self.y)
	def Translate(self,X,Y):
		self.x=self.x+Y
		self.y=self.y+X

obj=Point()
obj.Display()
obj.Translate(3,9)
obj.Display()
obj.Translate(2,1)
obj.Display()

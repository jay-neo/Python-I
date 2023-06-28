class Shape:
	def __init__(self,c):
		self.colour=c
class Retanagle(Shape):
	def __init__(self,l,b,class_Shape):
		self.length=l
		self.breadth=b
		self.colour=class_Shape.colour
	def calc_area(self):
		self.area=self.length*self.breadth
		return self.area
	def Rect_Details(self):
		print("For This Rectangle:")
		print("Colour =",self.colour)
		print("Length =",self.length)
		print("Breadth =",self.breadth)
		print("Area =",self.area)
class Triangle(Shape):
	def __init__(self,b,h,class_Shape):
		self.base=b
		self.height=h
		self.colour=class_Shape.colour
	def calc_area(self):
		self.area=0.5*self.base*self.height
		return self.area
	def Tring_Details(self):
		print("For This Triangle:")
		print("Colour =",self.colour)
		print("Base =",self.base)
		print("Height =",self.height)
		print("Area =",self.area)


obj_sp=Shape(90480)
obj_rec=Retanagle(5,6,obj_sp)
obj_tri=Triangle(2,3,obj_sp)
print(obj_rec.calc_area())
print(obj_tri.calc_area())
print(obj_rec.Rect_Details())
print(obj_tri.Tring_Details())
class Circle:
	def __init__(self,r):
		self.radius=r
	def get_radius(self):
		return self.radius
	def calc_area(self):
		area=(22/7)*(self.radius**2)
		return area

class Cylinder(Circle):
	def __init__(self,h,class_Circle):
		self.height=h
		self.radius=class_Circle.radius
		#self.radius=class_Circle.get_radius()
	def Calc_area(self):
		Area=2*(22/7)*self.radius*self.height
		return Area

r1=int(input("Enter the radius of circle = "))
h1=int(input("Enter the height of cylender = "))
obj_cir=Circle(r1)
obj_cycl=Cylinder(h1,obj_cir)
Area=round(obj_cycl.Calc_area(),2)
print(Area)

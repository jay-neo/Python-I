class Circle:
	def __init__(self,r):
		self.radius=r
	def get_radius(self):
		return self.radius
	def calc_area(self):
		area=(22/7)*(self.radius**2)
		return area

rad=int(input("Enter the radius of circle = "))
obj=Circle(rad)
print(obj.get_radius())
a=round(obj.calc_area(),2)
print(a)


x=eval(input("Enter first veriable = "))
y=eval(input("Enter second veriable = "))
X=x
Y=y

print("With third veriable")
temp=x
x=y
y=temp
print("First veriable =",x)
print("second veriable =",y)

print("Without using third veriable")
X=X+Y
Y=X-Y
X=X-Y
print("First veriable =",X)
print("second veriable =",Y)


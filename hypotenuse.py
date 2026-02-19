#Program to compute the length of hypotenuse (c) of a Right angled triangle Pythagoras theorem.

a=float(input("Enter the length of Perpendicular (p) of the triangle : "))
b=float(input("Enter the length of Base (b) of the triangle : "))

c=(a*a + b*b)**0.5

print("The Hypotenuse of the Right angled triangle is :", c)

#Program to Check whether quadratic equation has real roots or imaginary roots.
#Display the roots.

print("For a quadratic equation of the form ax^2 + bx + c = 0")
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

if a==0 :
    print("Please enter a non zero value for a.")
else :
    d = b**2 - 4*a*c
    if d >= 0:
        print("\nThe roots are Real.")
        sqrt_d = d**0.5
        root1 = (-b + sqrt_d) / (2 * a)
        root2 = (-b - sqrt_d) / (2 * a)
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    else:
        print("\nThe roots are Imaginary.")

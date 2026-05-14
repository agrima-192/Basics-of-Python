#Program to Print Fibonacci series up to given term.

print("This program prints Fibonnaci Series.")
n=int(input("Enter upto how many terms? "))
a,b=0,1

for i in range(n):
    print(a)
    a,b=b,a+b

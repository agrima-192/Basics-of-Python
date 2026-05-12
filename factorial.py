#Program to find the factorial of given number.

n=int(input("Enter the number to calculate its Factorial: "))
fact=1

for i in range(1,n+1):
    fact*=i

print("The factorial of",n,"is :",fact)

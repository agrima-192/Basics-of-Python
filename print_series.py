# Program to print the sum of the following series:
# 1+ ½ + 1/3 + ¼ +….+1/n

n=int(input("Enter the value of n: "))

sum_series=0.0

for i in range(1, n+1):
    sum_series += 1/i

print(f"The sum of the series up to {n} terms is: {sum_series:.4f}")


#Scan n values from 0-3 & print number of times each value occurred

n = int(input("Enter the number of values (n): "))
values = []

print(f"Enter {n} values between 0 and 3:")
for i in range(n):
    val = int(input(f"Value {i+1}: "))
    values.append(val)

counts = [0, 0, 0, 0]

for val in values:
    if 0 <= val <= 3:
        counts[val] += 1

for i in range(4):
    print(f"Value {i} occurred {counts[i]} times")

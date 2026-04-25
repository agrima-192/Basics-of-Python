#Program to find whether a given number is in sequence (10,20,56,78,89) using membership operator.

sequence = (10, 20, 56, 78, 89)
num = int(input("Enter the number to be checked in the sequence : "))

if num in sequence:
    print("The number",num,"is present in the sequence.")
else:
    print("The number",num,"is NOT present in the sequence.")

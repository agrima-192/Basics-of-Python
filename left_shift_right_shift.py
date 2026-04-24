#Program to find left shift and right shift values of a given number.

num = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to shift: "))

left_shift = num << shift     # Left Shift

right_shift = num >> shift    # Right Shift

print(f"Original Number: {num}")
print(f"Left Shift by {shift}: {left_shift}")
print(f"Right Shift by {shift}: {right_shift}")

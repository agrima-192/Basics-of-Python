#Program to print truth table for bitwise operators (&, | and ^ operators)

print("---- Truth Table for Bitwise Operators (0 & 1 inputs) ----\n")

print("|    A    |    B    |    A&B    |    A|B    |    A^B    |")
print("-" * 57)

for a in [0,1]:
    for b in [0,1]:
        print(f"|    {a}    |    {b}    |     {a&b}     |     {a|b}     |     {a^b}     |")

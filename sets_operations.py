#Program to Take two sets & apply various set operations on them :
#S1 = {Red ,yellow, orange , blue}
#S2 = {violet, blue , purple}

S1 = {"Red","yellow","orange","blue"}
S2 = {"violet","blue","purple"}

print(f"Set S1: {S1}")
print(f"Set S2: {S2}")
print("-" * 70)

print("Union:",S1|S2,'\n')

print("Intersection:",S1&S2,'\n')

print("Difference (S1-S2):",S1-S2,'\n')

print("Symmetric Difference:",S1^S2,'\n')

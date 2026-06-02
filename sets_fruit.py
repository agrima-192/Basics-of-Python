#Create 2 sets s1 and s2 of n fruits each by taking user input & find:
""" a)	Fruits which are in both sets s1 and s2
    b)	Fruits only in s1 but not in s2
    c)	Count of all fruits from s1 and s2   """


n = int(input("Enter n: "))
s1 = set()
s2 = set()

print(f"Enter {n} fruits for Set 1:")
for _ in range(n):
    s1.add(input().strip().lower())

print(f"Enter {n} fruits for Set 2:")
for _ in range(n):
    s2.add(input().strip().lower())

print("a) In both:", s1 & s2)
print("b) Only in s1:", s1 - s2)
print("c) Total count:", len(s1 | s2))

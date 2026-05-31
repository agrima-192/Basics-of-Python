#Program to count number of occurrences of each
#alphabet (case insensitive) & display it

text=input("Enter a string: ")
text=text.upper()

counts={}
for char in text:
    if char.isalpha():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

for char, count in counts.items():
    print(f"{count}{char}")

#Program to Count total number of vowels in a given string.

s=input("Enter a string : ")
v="aeiou"        #v=['a','e','i','o','u']
s=s.lower()
count=0
for i in s:
    if i in v:
        count+=1
print(count)

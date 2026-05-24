#Program to count & display the number of capital letters in a string.

n=input("Enter a String: ")
count=0
for i in n:
    if 'A'<= i <= 'Z' :
        count+=1
print(count)


"""n=input("Enter a String: ")
count=0
for i in n:
    if chr(65) <= i <= chr(90):
        count +=1
print(count)"""

"""n=input("Enter a String: ")
count=0
for i in n:
    if i.isupper():
        count+=1
print(count)"""

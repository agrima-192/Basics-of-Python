# Program to check whether given number is palindrome or not.

num=int(input("Enter a number : "))

temp=num
rev=0

while (temp>0):
    rem=temp%10
    rev=rev*10 + rem
    temp//=10

if rev==num :
    print(f"The number {num} is a Palindrome.")
else :
    print(f"The number {num} is NOT a Palindrome.")


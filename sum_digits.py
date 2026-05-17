# Program to print sum of digits of a number.

num=int(input("Enter a number: "))

Sum=0
temp=num

while temp>0 :
    digit=temp%10
    Sum+=digit
    temp//=10

print("The sum of digits of",num,"is :",Sum)

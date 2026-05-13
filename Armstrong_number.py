# Program to find whether the given number is Armstrong number.

num=int(input("Enter a number to check whether it is Armstrong or not : "))

temp=num
sum_digits=0
power=len(str(num))

while temp>0 :
    digit=temp%10
    sum_digits+=digit**power
    temp//=10

if sum_digits==num :
    print(f"{num} is an Armstrong number.")
else :
    print(f"{num} is NOT an Armstrong number.")

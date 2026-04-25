#Program to check whether the given number is divisible by 3 and 5 both.

x=int(input("Enter a number to check : "))

if x%3==0 and x%5==0 :
    print ("The number",x,"is divisible by 3 and 5.")
else :
    print ("The number",x,"is NOT divisible by 3 and 5.")

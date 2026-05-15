# Program to find if the given number is prime number or not.

num=int(input("Enter a number: "))

if num>1 :
    for i in range(2, int(num**0.5)+1):
        if num%i==0 :
            print(f"{num} is NOT a Prime number.")
            break
    else :
        print(f"{num} is a Prime number.")
else:
    print(f"{num} is NOT a Prime number.")





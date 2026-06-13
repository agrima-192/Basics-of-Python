#Create a tuple to store n numeric values & find average of all values

n=int(input("Enter number of values:"))
a=[]

for i in range(n):
    a.append(int(input("Enter element:")))
t=tuple(a)
sum=0

for i in t:
    sum=sum+i
avg=sum/n
print(t)
print("Average:",avg)

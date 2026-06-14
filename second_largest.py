#Program to input a list of scores for N students in a list data type.
#Find the score of the runner-up and print the output.

n=int(input("Enter the value of n:"))
a=[]

for i in range(n):
    a.append(int(input("Enter element:")))
g=a[0]
sg=a[1]

if sg>g:
    g,sg=sg,g
for i in a:
    if(g<i):
        sg=g
        g=i
    elif(i<g and sg<i):
        sg=i
        
print(sg)

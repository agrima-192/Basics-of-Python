#Program to enter a string and a substring
#& print the number of times that the substring occurs in the given string.
#String traversal will take place from left to right, not from right to left.

string=input("Enter a String : ")
substr=input("Enter a Sub-string to check: ")

count=0
start=0

while True :
    pos=string.find(substr,start)
    if pos==-1:
        break
    count+=1
    start=pos+1
    
print(count)

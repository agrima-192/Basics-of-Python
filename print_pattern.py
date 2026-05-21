# Pogram to print the following pattern
'''
123454321
1234 *4321
123  * * 321
12   * * *  21
1    * * * *   1
'''

n=5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    
    num_stars = n - i
    for k in range(num_stars):
        print("*", end="")
        
    for j in range(i, 0, -1):
        if i == n and j == n:
            continue
        print(j, end="")
    print()


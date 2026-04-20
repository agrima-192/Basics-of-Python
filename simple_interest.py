#Program to find Simple Interest

P=int(input("Enter the Principal Amount (in rupees): "))
R=float(input("Enter the Rate of Interest (in percentage): "))
T=float(input("Enter the Time of Interest (in years): "))

SI=(P*R*T)/100

print("The Simple Interest is :", SI)
print("The Total Amount is :", SI+P)

#Program to convert given seconds into hours, minutes and remaining seconds.

time=int(input("Enter the Time in seconds: "))

hours = time // 3600
remaining_seconds = time % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours:",hours,"Minutes:",minutes,"Seconds:",seconds)

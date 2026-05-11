#Print the grade sheet of a student for the given range of cgpa.
#Scan marks of five subjects and calculate the percentage.

name = input("Enter Name: ")
roll_no = input("Enter Roll Number: ")
sap_id = input("Enter SAPID: ")
semester = input("Enter Semester: ")
course = input("Enter Course: ")

subjects = ["PDS", "Python", "Chemistry", "English", "Physics"]
marks = []
for sub in subjects:
    m = float(input(f"Enter marks for {sub}: "))
    marks.append(m)

percentage = sum(marks) / len(subjects)
cgpa = percentage / 10

if 0 <= cgpa <= 3.4:
    grade = "F"
elif 3.5 <= cgpa <= 5.0:
    grade = "C+"
elif 5.1 <= cgpa <= 6.0:
    grade = "B"
elif 6.1 <= cgpa <= 7.0:
    grade = "B+"
elif 7.1 <= cgpa <= 8.0:
    grade = "A"
elif 8.1 <= cgpa <= 9.0:
    grade = "A+"
elif 9.1 <= cgpa <= 10.0:
    grade = "O (Outstanding)"
else:
    grade = "Invalid Input"

print("\n" + "="*30)
print(f"      STUDENT GRADESHEET")
print("="*30)
print(f"Name       : {name}")
print(f"Roll No    : {roll_no}")
print(f"SAPID      : {sap_id}")
print(f"Semester   : {semester}")
print(f"Course     : {course}")
print("\n")

for sub, score in zip(subjects, marks):
    print(f"{sub:<10} : {score}")

print(f"Percentage : {percentage}%")
print(f"CGPA       : {cgpa:.1f}")
print(f"Grade      : {grade}")

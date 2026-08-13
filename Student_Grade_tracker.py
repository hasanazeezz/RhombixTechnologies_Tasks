print("Student Grade Tracker")

name = input("Enter student name: ")

subjects = int(input("How many subjects do you have? "))

total = 0

for i in range(1, subjects + 1):
    marks = float(input("Enter marks for Subject " + str(i) + " (0-100): "))
    total = total + marks

average = total / subjects

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Final Grade:", grade)
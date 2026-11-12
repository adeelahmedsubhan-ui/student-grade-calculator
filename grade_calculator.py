
name = input("Enter Student Name: ")

english = float(input("Enter English Marks: "))
math = float(input("Enter Math Marks: "))
physics = float(input("Enter Physics Marks: "))
computer = float(input("Enter Computer Marks: "))
programming = float(input("Enter Programming Marks: "))

total = english + math + physics + computer + programming
percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)

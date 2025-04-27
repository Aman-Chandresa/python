def get_grade(marks):
    if marks == 0:
        print("NA")
    elif 0 <= marks <= 39:
        print("F")
    elif 40 <= marks <= 44:
        print("P")
    elif 45 <= marks <= 49:
        print("C")
    elif 50 <= marks <= 54:
        print("B")
    elif 55 <= marks <= 59:
        print("B+")
    elif 60 <= marks <= 69:
        print("A")
    elif 70 <= marks <= 79:
        print("A+")
    elif 80 <= marks <= 100:
        print("O")

def check_pass_or_fail(marks):
    if marks <= 39:
        print("Fail")
    else:
        print("Pass")

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print(f"Total Marks: {total}")
print(f"Average Marks: {average}")

print("Subject 1:")
get_grade(marks1)
check_pass_or_fail(marks1)

print("Subject 2:")
get_grade(marks2)
check_pass_or_fail(marks2)

print("Subject 3:")
get_grade(marks3)
check_pass_or_fail(marks3)

print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
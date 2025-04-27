def check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
result = check(number)

print(f"The number {number} is {result}.")
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
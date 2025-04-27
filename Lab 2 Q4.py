def div(number):
    if number % 10 == 0:
        return "divisible by 10"
    else:
        return "not divisible by 10"

number = int(input("Enter a number: "))
result = div(number)

print(f"The number {number} is {result}.")
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
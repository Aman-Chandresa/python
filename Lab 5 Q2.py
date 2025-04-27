numbers = [12, 7, 25, 7, 18, 7, 30, 15, 22, 7, 27, 40, 7, 35, 45, 7, 50, 5, 7, 10]
print("List:", numbers)

num = int(input("Enter a number to find its positions: "))

positions = []
for index, value in enumerate(numbers):
    if value == num:
        positions.append(index)

if positions:
    print("The number", num, "is found at positions:", positions)
else:
    print("The number", num, "is not found in the list.")
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
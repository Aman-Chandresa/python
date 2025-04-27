numbers = [5, -12, 7, -5, 18, 22, -7, 9, 12, -30,
           18, 22, -7, 3, -9, 25, -5, 18, 12, -22,
           7, -9, 30, 18, -25, 5, -12, 22, 7, -30]

print("Original list:", numbers)

positive_numbers = []
negative_numbers = []

for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

print("Positive numbers list:", positive_numbers)
print("Negative numbers list:", negative_numbers)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
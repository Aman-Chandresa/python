numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           5, 7, 12, 18, 22, 25, 30, 3, 9, 15,
           1, 6, 10, 14, 19, 23, 27, 28, 2, 4]

print("Original list with duplicates:", numbers)

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
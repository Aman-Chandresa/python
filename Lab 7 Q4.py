input_string = input("Enter a string: ")
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("Character frequency in the string:", char_frequency)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
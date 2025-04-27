string = input("Enter a string: ")
def vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print("Number of vowels in the string:", count)
vowels(string)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
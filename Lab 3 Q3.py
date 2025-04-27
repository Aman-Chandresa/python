string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
def string(string1, string2):
    if string2 in string1:
        print(f"{string2} is present in {string1}")
    else:
        print(f"{string2} is not present in {string1}")
string(string1, string2)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
def xyz(a, b, c):
    if a > b and a > c:
        largest = a
    else:
        largest = b if b > c else c

    if a < b and a < c:
        smallest = a
    else:
        smallest = b if b < c else c

    return largest, smallest

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
c = float(input("Enter third value: "))
largest, smallest = xyz(a, b, c)

print("Largest value:", largest)
print("Smallest value:", smallest)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
def xyz(a, b):
    if a > b:
        largest = a
        smallest = b
    else:
        largest = b
        smallest = a
    
    return largest, smallest

a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
largest, smallest = xyz(a, b)

print("Largest value:", largest)
print("Smallest value:", smallest)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
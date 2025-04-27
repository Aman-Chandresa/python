length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

def compare(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    if area > perimeter:
        return "Area is greater than perimeter"
    elif area < perimeter:
        return "Perimeter is greater than area"
    else:
        return "Area and perimeter are equal"
print(compare(length, breadth))
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
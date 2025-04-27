angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))
def xyz (angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid triangle")
    else:
        print ("Invalid triangle")
print(xyz(angle1, angle2, angle3))
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
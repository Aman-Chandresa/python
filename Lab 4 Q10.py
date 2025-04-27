num = int(input("Enter N: "))
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(num)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
def triplets():
    for a in range(1, 31):
        for b in range(a, 31):
            c = (a**2 + b**2) ** 0.5
            if c == int(c) and c <= 30:
                print(a, b, int(c))
triplets()
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
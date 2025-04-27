def hours():
    for hour in range(24):
        if hour == 0:
            print("12 AM - Midnight")
        elif hour == 12:
            print("12 PM - Noon")
        elif hour < 12:
            print(f"{hour} AM")
        else:
            print(f"{hour - 12} PM")
hours()
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
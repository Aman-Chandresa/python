names = [("Aman", "Sneh"), ("Samay", "Krish"), "Ayesha", "Khushi", ("Harsh", "Jeet"), "Dhruvi"]

boys_count = 0
girls_count = 0

for ele in names:
    if isinstance(ele, tuple):
        boys_count += 1
    else:
        girls_count += 1

print("Number of boys:", boys_count)
print("Number of girls:", girls_count)
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
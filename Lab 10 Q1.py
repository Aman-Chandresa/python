import csv
filename = "sample.csv"
header = ['Name', 'Age', 'City']
rows = [
    ['Aman', 18, 'Gandhidham'],
    ['Samay', 18, 'Surat'],
    ['Krish', 19, 'Vadodara']
]
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
print(f"CSV file '{filename}' created successfully.")
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
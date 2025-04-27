employees = {
    101: [(1, 50000), (2, 60000), (3, 55000)],  
    102: [(4, 70000), (5, 65000), (6, 80000)],  
    103: [(7, 45000), (8, 50000), (9, 55000)]  
}

for dept_no, emp_list in employees.items():
    salaries = [emp[1] for emp in emp_list]
    min_salary = min(salaries)
    max_salary = max(salaries)
    
    print(f"Department {dept_no} - Minimum Salary: {min_salary}, Maximum Salary: {max_salary}")
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
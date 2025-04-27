def filter_names(names):
    return [name for name in names if len(name) > 8]
def main():
    names = ['Amit', 'Suresh', 'Bhupendra', 'Priyanka', 'Mahendra', 'Krishna', 'Vishal', 'Nandini']
    updated = filter_names(names)
    print(updated)
main()
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
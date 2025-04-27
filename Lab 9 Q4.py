def is_palindrome(word):
    if isinstance(word, str) and word == word[::-1]:
        return True
    return False
def main():
    lst = ['madam', 'Python', 'malayalam', 12321]
    for item in lst:
        if is_palindrome(item):
            print(item)
main()
print("Name: Aman Chandresa")
print("Roll Number: 24BCL003")
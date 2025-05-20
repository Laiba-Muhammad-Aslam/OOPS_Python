def is_palindrome_number(num):
    return str(num) == str(num)[::-1]

print(is_palindrome_number(121))  
print(is_palindrome_number(123))  

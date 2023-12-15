# An integer as input and returns true if it is palindrome false if it is not.

def ispalindrome(num):
    number_str = str(num)
    return number_str == number_str[::-1]
values = 11
values_1 = ispalindrome(values)
print(values_1)

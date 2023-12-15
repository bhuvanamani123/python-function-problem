
"""31. AddForThird : Given three numbers a, b and c,
return true if the sum of any two equals the third
number"""


def add_for_third(a, b, c):
    return a + b == c or a + c == b or b + c == a


num_a = int(input("Enter the first number: "))
num_b = int(input("Enter the second number: "))
num_c = int(input("Enter the third number: "))

result = add_for_third(num_a, num_b, num_c)

print({'True' if result else 'False'})


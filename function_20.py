"""NumberInAscendingOrder : Given 3 numbers -
num1, num2 and num3 as input, return true if they are
in ascending order. Important - Do not use if
statement in solution."""


def number_in_ascending_order(num1, num2, num3):
    return num1 < num2 < num3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = number_in_ascending_order(num1, num2, num3)

print(result)

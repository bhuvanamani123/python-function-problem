"""LargerThanOne : Given three numbers as input,
num1, num2 and num3, return true if num1 is greater
than at least one of num2 and num3. Do not use if
statement to solve this problem."""

def number_in_ascending_order(num1, num2, num3):
    return num1 < num2 < num3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = number_in_ascending_order(num1, num2, num3)

print(result)

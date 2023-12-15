"""SameLastDigit : Given 2 non negative numbers a
and b, return true if both of them have the same last
digit."""

def digit(a, b):
    return str(a)[-1] == str(b)[-1]

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = digit(num1, num2)

print(result)

"""SumLast3 : Given a number as input, return the sum
of its last 3 digits."""

def sum(number):
     return sum(map(int, str(number)[-3:])) if number >= 100 else "Please enter a number with at least 3 digits."


input_number = int(input("Enter a number: "))
result = sum(input_number)

print(result)
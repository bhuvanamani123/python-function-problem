"""Write a function to generate even numbers from
FROM to TO ( you should not write the logic to check
if number is even or not, instead you should call
isEven() method which you create earlier). 43b) do the
same without using if condition."""

def is_even(number):
    return number % 2 == 0

def even_numbers_without_if(from_num, to_num):
    return [num for num in range(from_num, to_num + 1) if is_even(num)]
from_number, to_number = map(int, input("Enter the starting and ending numbers (space-separated): ").split())
result = even_numbers_without_if(from_number, to_number)

print(" {from_number} to {to_number} are: {result}")

"""Write a method to generate prime numbers
between from and to ( you should not write the logic
to check if number is prime or not, instead you should
call isPrime() method which you create earlier)."""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime_numbers(from_num, to_num):
    return [num for num in range(from_num, to_num + 1) if is_prime(num)]

# Example usage:
from_number, to_number = map(int, input("Enter the starting and ending numbers (space-separated): ").split())
result = generate_prime_numbers(from_number, to_number)

print("{from_number} to {to_number} are: {result}")

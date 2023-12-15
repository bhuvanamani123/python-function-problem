#An integer is input and returns true if it is prime false if it’s not.

def prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

start = int(input("Enter a number: "))
end = int(input("Enter a number: "))

for num in range(start, end + 1):
    if prime(num):
        print(num, end=",")

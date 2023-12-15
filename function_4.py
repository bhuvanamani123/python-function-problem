#A function which accepts a number as input and returns the Factorial of that number.

def factorial(number):
    if number<0:
        print("negative value")
    elif number == 0:
        return 1
    else:
        return number *factorial(number-1)  
    
print(factorial(-20))
print(factorial(50))
print(factorial(90))
print(factorial(90))
print(factorial(100))



"""An integer as input and returns a Fibonacci series of
that size. For this, you need to study arrays since we
haven't studied arrays yet you can store all the numbers in
a string and return the string itself. Do the same for similar
questions."""


def fibonacci_series(size):
    if size <= 0:
        return "Invalid input."

    fib_series = "0, 1"  

    while len(fib_series.split(", ")) < size:
       
        next_num = int(fib_series.split(", ")[-1]) + int(fib_series.split(", ")[-2])
        fib_series += f", {next_num}"

    return fib_series
size_input = int(input("Enter Fibonacci series: "))

result = fibonacci_series(size_input)

print(result)

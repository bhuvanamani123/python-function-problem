#Given a 4 digit number as input, find the value of its
#hundredth digit. Ip: 1234 op:2


def digit_number(number):
    return (number // 100)%10 if 1000<=number<=9999 else None
num = 858
values = digit_number(num)
print(values) if values is not None else print("this values is not 4 digit values") 
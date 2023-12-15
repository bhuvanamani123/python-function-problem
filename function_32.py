"""LotteryPrize: Jack bought a lottery ticket. He will get
a reward based on the number of lottery tickets. The
rules are as follows - If the ticket number is divisible
by 4, he gets 6 - If the ticket number is divisible by 7,
he gets 10 - If the ticket number is divisible by both 4
and 7, he gets 20 Otherwise, he gets 0. Given the
number of the lottery ticket as input, compute the
reward he will receive"""

def lotter_prize(tic_number):
    if tic_number%4==0 and tic_number%7==0:
       return 20
    elif tic_number % 4 == 0:
        return 6
    elif tic_number % 7 == 0:
        return 10
    else:
        return 0
    
tic_number = int(input("enter the ticket number: ")) 
values = lotter_prize(tic_number)
print(values)   
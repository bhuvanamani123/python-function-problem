"""LotteryPrize3 : Jack bought 3 lottery tickets. He will
get a reward based on the number of the lottery ticket.
The rules are as follows - If the ticket number is
divisible by 4, he gets 6 - If the ticket number is
divisible by 7, he gets 10 - If the ticket number is
divisible by both 4 and 7, he gets 20 - Otherwise, he
gets 0. Given the numbers of the 3 lottery tickets as
input, compute the total reward he will receive. In this
problem define a function to compute the reward
given the ticket number and use that function to
calculate the total reward"""


def lottery_prize(number):
    if number % 4 == 0 and number % 7 == 0:
        return 20
    elif number % 4 == 0:
        return 6
    elif number % 7 == 0:
        return 10
    else:
        return 0

tickets = [int(input("Enter ticket number 1: ")), int(input("Enter ticket number 2: ")), int(input("Enter ticket number 3: "))]

total_reward = sum(lottery_prize(ticket) for ticket in tickets)

print(total_reward)


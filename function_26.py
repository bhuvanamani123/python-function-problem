"""DaysInMonth : Given the number of the month and
year as input (1 for January, 12 for December), return
the number of days in it. Ip: 1, 2019 op: 31, ip:2,2020
op: 29."""
import calendar

def days_in_month(month, year):
    days = calendar.monthrange(year, month)[1]
    return days

month_input = int(input("Enter the month (1 for January, 12 for December): "))
year_input = int(input("Enter the year: "))

result = days_in_month(month_input, year_input)

print(result)


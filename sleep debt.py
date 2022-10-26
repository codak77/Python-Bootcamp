desirable_amount_of_sleep = 56
total_sleep = 0

for x in range(1, 28):
    print("day :", x)
    actual_amount_of_sleep = float(input("Enter the amount of sleep: "))
    total_sleep += actual_amount_of_sleep

if total_sleep != desirable_amount_of_sleep:
    print("you are jealousy, you do not have sleep debit")
else:
    print("You have sleep debit")

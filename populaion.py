number = int(input("Enter the starting number of organisms: "))

increasing_percentage = int(input("Enter the average daily increase: "))

days = int(input("Enter the number of days: "))

print("Days Approximate \tPopulation")
for x in range(1, days+1):
    if x > 1:
        increase = number * increasing_percentage / 100
        number += increase

print(x, "\t\t\t", format(number, '.2f'))

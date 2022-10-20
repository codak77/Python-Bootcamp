import numbers


principalAmount = float(input("Please enter the principal amount  $"))
print("\n")

annualInterest = float(input("Please enter the annual interest rate % : "))
print("\n")

numb_int_cmpnded = float(
    input("Please enter the number of times per year interest has compounded : "))
print("\n")

number_years = float(
    input("Enter the number of years account will be left to earn interest : "))
print("\n")

annualInterest /= 100

answer = principalAmount * \
    ((1 + (annualInterest / numb_int_cmpnded)) ** (numb_int_cmpnded * number_years))

print("After", " ", number_years, " ", "years, $", format(
    answer, ",.2f"), " ", "will be in the account.", sep="")

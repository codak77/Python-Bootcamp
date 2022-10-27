
"""
def my_func(name,place):
  print(f"Hello {name}! Are you from {place}?")
"""

"""
def total_calc(bill_amount,tip_perc=10):
  total = bill_amount*(1 + 0.01*tip_perc)
  total = round(total,2)
  print(f"Please pay ${total}")
"""

"""
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
"""

"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""


def fizz_buzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))

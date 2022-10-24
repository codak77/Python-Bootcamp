"""
# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y':

    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

# Calculate the commission.
    commission = sales * comm_rate

# Display the commission.
    print('The commission is $',
          format(commission, ',.2f'), sep='')

# See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' +
                       'commission (Enter y for yes): ')
"""

# This program displays property taxes.

TAX_FACTOR = 0.0065  # Represents the tax factor.

# Get the first lot number.
print('Enter the property lot number')
print('or enter 0 to end.')

lot = int(input('Lot number: '))

# Continue processing as long as the user
# does not enter lot number 0.
while lot != 0:
    # Get the property value.
    value = float(input('Enter the property value: '))

# Calculate the property's tax.
    tax = value * TAX_FACTOR

# Display the tax.
print('Property tax: $', format(tax, ',.2f'), sep='')

# Get the next lot number.
print('Enter the next lot number or')
print('enter 0 to end.')
lot = int(input('Lot number: '))

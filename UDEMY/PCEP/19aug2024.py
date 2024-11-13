
#Python Refund Checker

# Get user inputs
a = int(input('How many days ago have you purchased the item? '))  # Days since purchase
b = input('Have you used the item at all [y/n]? ')  # Whether the item has been used
c = input('Has the item broken down on its own [y/n]? ')  # Whether the item has broken down on its own

# Check refund conditions
if (c == 'y' and a < 31) or b == 'n':  # If the item broke down on its own within 31 days, or if it has never been used
    print('You can get a refund.')  # Print refund message
else:
    print("You can't get a refund.")  # Print no refund message






a = int(input('How many days ago have you purchased the item? '))
b = input('Have you used the item at all [y/n]?  ')
c = input('Has the item broken down on its own [y/n]? ')

if c == 'y' and  a < 31 or b == 'n':
    print('You can get a refund.')
else:
    print("You can't get a refund.")



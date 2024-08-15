# 1. practicing escaping characters and using special characters with print()
print('::print()::')
print('I\'m learning to become a Python developer!\nI\'m so excited!')

"""
1. USE CASE
Let's practice the print() function. Show the following message to the output:

I'm learning to become a Python developer!
I'm so excited!
"""

print('\n-----------------------------------------------\n')


# 2. Creating variables 
print('::Creating Variables::')

stringVariable = 'stringVariable reporting for duty!'
integerVariable = 444
floatVariable = 4.44 
booleanVariableTrue = True
booleanVariableFalse = False

print ('I have created a few variables:')
print ('\t string:', stringVariable)
print('\t integer:', integerVariable)
print('\t float:', floatVariable)
print('\t True boolean:', booleanVariableTrue) 
print('\t False boolean:', booleanVariableFalse)

"""
2. USE CASE
Try creating a string, integer, float and boolean variables. Then print them using print(). 
"""

print('\n-----------------------------------------------\n')

# 3. Variables and OperatorsTroy

print('::Variables and Operators::')

income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 'income tax in Ripoffland. You would save',income *  ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')

"""
3. USE CASE

In a fictional country named Lowtaxland, the income tax is 5%. In another fictional country, Ripoffland, the income tax is 43%. You are given a sample variable named income with the value of 250,000.

1. Create two additional variables: lowtaxland_rate with the value of 0.05 (which is the same as 5%) and ripoffland_rate with the value of 0.43 (which is the same as 43%).
*
2. Print to the output the following (all output on a single line):

Your income is {income} and you would pay {tax amount in Lowtaxland} income tax in Lowtaxland or {tax amount in Ripoffland} income tax in Ripoffland. You would save {difference between the tax amounts} by paying taxes in Lowtaxland!

Your solution must replace the curly brackets (e.g. {income}) with the actual values (e.g. 250000). The values must be calculated correctly. The tax amount should be calculated as {income * lowtaxland_rate} for Lowtaxland, and {income * ripoffland_rate} for Ripoffland, respectively.
"""

print('\n-----------------------------------------------\n')

# 4. Getting User input with input() pt.1 
print('::input()::')
print('What is your name?')
user_name = input()
print('Hello,', user_name) 

'''
4. USE CASE

Just a basic example

'''

print('\n-----------------------------------------------\n')

# 5. Getting User input with input() pt.2 
print('::input()::')

_login = input('Enter your login: ')
_language = input('Enter your native language: ')
print('Your login is', _login, 'and you speak', _language)

'''
5. USE CASE

Ask the user to provide their login and native language. Use the following prompts:

Enter your login: << remember to add a space at the end of this prompt!
Enter your native language: << remember to add a space at the end of this prompt!

Then, show the user the following message:

Your login is {login provided} and you speak {language provided}

For example, if the user provides the login h_potter and language British English, show:

Your login is h_potter and you speak British English
'''

print('\n-----------------------------------------------\n')

# 6. Typecasting! Creating a Wage Calculator

print('::Wage Calculator::')

hours = float(input('How many hours did you work last month? '))
hourly_rate = float(input('What is your hourly rate? '))
print('Last month, you earned', hours * hourly_rate, 'dollars')

"""
6. USE CASE 
Ask the user for the number of hours they worked last month and their hourly rate (both numbers should be floats). Use the following prompts:

How many hours did you work last month? << add a space at the end of this prompt
What is your hourly rate? << add a space at the end of this prompt

Then, show the following message with the calculated salary:

Last month, you earned {hours * hourly_rate} dollars

The salary should be shown as a float number. For example, for input 30 hours and hourly rate 10.5, show:

Last month, you earned 315.0 dollars
"""



'''
EC2 Random Name Generator

FOUNDATIONAL
Several departments share an AWS environment. 
You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
Use Python to create your unique EC2 names that the users can then attach to the instances. 
The Python Script should:
    1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
    2. Allow the user to input the name of their department that is used in the unique name.
    3. Generate random characters and numbers that will be included in the unique name.
    4. Push your code to GitHub...

ADVANCED
The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments. List these departments as options and if a user puts another department, print a message that they should not use this Name Generator. Be sure to account for incorrect upper or lowercase letters in the correct department. Example: a user inputs accounting vs Accounting.

COMPLEX
Turn the above into a Function and execute the Function to verify it works.

'''
print('EC2 Random Name Generator')
level_choice = int(input('\n \t  1. Foundational: \n \t  2. Advanced: \n \t  3. Complex: \n \t      Enter 1-3 to choose a level: '))

def P1F():
    import random
    howManyEC2 = int(input(' \n Enter a Number for How many EC2 instances you need names generated for: ')) # The number of EC2 names that will be generated
    EC2namesList = []  # a place to store the generated names with .append
    DepartmentName = str(input('\n Enter Your Department name: ')) # grab a department name from the user
   
    for i in range(howManyEC2):
        EC2nameGenerator = f"{DepartmentName}-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k = 8))}"
        EC2namesList.append(EC2nameGenerator)
    
    return EC2namesList
        
    # We Should Check to make sure there are no duplicates in the list generated.
    # We Should Check to make sure none of the names generated match any of the names in existing EC2 instances.

def P1A():
    import random
    import sys

    howManyEC2 = int(input(' \n Enter a Number for How many EC2 instances you need names generated for: ')) # The number of EC2 names that will be generated
    EC2namesList = []  # a place to store the generated names with .append
    DepartmentName = str(input('\n \t  > Marketing: \n \t  > Accounting: \n \t  > FinOps: \n \t      Enter the name of your department: ')).strip().lower()
    ValidDepartmentNames = ['marketing', 'accounting', 'finops'] # Store the valid names
    
    #Check for Valid Department Name
    if DepartmentName in ValidDepartmentNames:
        # Generate System Name
        for i in range(howManyEC2):
            EC2nameGenerator = f"{DepartmentName}-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k = 8))}"
            EC2namesList.append(EC2nameGenerator.upper())

        #Check the Contents of EC2namesList
        for x in EC2namesList:
            print(x)

        #Return EC2namesList and exit the function
        return EC2namesList

    else: 
            print('Department Error: Only Marketing, Accounting and FinOps are allowed.')
            sys.exit()        
    
def P1C():
    P1A() # Well is is just a repeat of what we have already done. So let's Just call it again. 


if level_choice == 1:
    P1F()
elif level_choice == 2:
    P1A()
elif level_choice == 3:
    P1C()
else:
    print('Choice Invalid. Exiting...')


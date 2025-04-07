import random

print('EC2 Random Name Generator')

def P1F():
    howManyEC2 = int(input(' \n Enter a Number for How many EC2 instances you need names generated for: ')) # The number of EC2 names that will be generated
    EC2namesList = []  # a place to store the generated names with .append
    DepartmentName = str(input('\n Enter Your Department name: ')) # grab a department name from the user
   
    for i in range(howManyEC2):
        EC2nameGenerator = f"{DepartmentName}-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k = 8))}"
        EC2namesList.append(EC2nameGenerator)
    
    #Check the Contents of EC2namesList
    for x in EC2namesList:
        print(x)
        
    return EC2namesList

#Call the function
P1F()


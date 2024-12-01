# this is a lesson in working with tupples and lists. 
'''
All Roads Lead to Rome
You are given a list with various flight connections in Europe. Each connection is represented as a tuple with the following elements:

(city_from, city_to, time)

For example, the following tuple represents a flight from Amsterdam to Dublin which takes 100 minutes:

('Amsterdam', 'Dublin', 100)

Your task is to go through all the routes in a loop and check how many of them lead to Rome (i.e. how many of them have city_to equal to 'Rome'). Among the routes to Rome, you should also calculate the average flight time. Print the following the output:

{} connections lead to Rome with an average flight time of {} minutes

Replace {} with the number of connections and the average flight time.
'''

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130), # tricky they said all roads to Rome not from
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
connection = 0
airtime = 0
avgtime = 0

for flight in connections:
    if 'Rome' in flight[1]: # specifying the specific element to check against solved the trick
        connection += 1
        airtime += flight[2]

if connection > 0 : #having an if statement to check the data
    avgtime = airtime / connection # calculating the average 1 time outside of the loop is for the best
    print(f"{connection} connections lead to Rome with an average flight time of {avgtime} minutes")
else:
    print(f"There are no flights to Rome") # adding an else statement just in case we change the data

'''
sample solution
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170)
    ]
 
counter = 0
sum = 0.0
 
for con in connections:
    if con[1] == 'Rome':
        counter += 1
        sum += con[2]
 
print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes') #they calculate in the string
'''
## Dictionaries. 

# Create Dictionary

#grades = {} #empty

grades = { # 4 keys with 4 values
    'Alice': 88,
    'Bob': 92,
    'Charlie': 75,
    'Diana': 95
}


#test 1 - empty dictionary

print(f"{grades} > test 1")


#test 2 - adding a value to a empty dictonary 
grades['Jacob'] = '82'

print(f"{grades} > test 2")

# test 3 - Remove the key 'Bob'
del grades['Bob']

print(f"{grades} > test 3") 


# test 4 - Modify Jacob to 73
grades['Jacob'] = '73'

print(f"{grades} > test 4")

#Notes
'''
1. Direct Assignment
As you already know, you can modify the value of a dictionary key by directly assigning a new value.

Example:
python
Copy code
grades = {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95}

# Modify Charlie's grade to 90
grades['Charlie'] = 90
2. Using update() Method
The update() method is used to update the dictionary with new key-value pairs. If a key already exists, the value is updated; if the key doesn't exist, it's added.

Example:
python
Copy code
grades = {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95}

# Update Charlie's grade to 90 and add a new student 'Eve' with grade 85
grades.update({'Charlie': 90, 'Eve': 85})

print(grades)
# Output: {'Alice': 88, 'Bob': 92, 'Charlie': 90, 'Diana': 95, 'Eve': 85}
update() can also take keyword arguments:

python
Copy code
grades.update(Charlie=90, Eve=85)
You can also merge two dictionaries using update():

python
Copy code
new_grades = {'Eve': 85, 'Frank': 78}
grades.update(new_grades)
3. Using setdefault() Method
The setdefault() method is used to get the value of a key, and if the key doesn't exist, it inserts the key with a default value. It’s often used when you want to add a default value if the key is missing.

Example:
python
Copy code
grades = {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95}

# Get the value of 'Charlie', or set it to 80 if it doesn't exist
charlie_grade = grades.setdefault('Charlie', 80)

print(grades)
# Output: {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95}

# Adding a new key with setdefault (this won't overwrite existing values)
grades.setdefault('Eve', 85)

print(grades)
# Output: {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95, 'Eve': 85}
If the key exists, setdefault() returns the current value.
If the key does not exist, it sets the key to the provided default value and returns that.
4. Using Dictionary Comprehension (for Bulk Modifications)
You can also modify a dictionary using dictionary comprehensions. This is especially useful when you want to modify the values based on some condition or apply a transformation to all values.

Example (e.g., incrementing all grades by 5):
python
Copy code
grades = {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95}

# Add 5 points to every grade in the dictionary
grades = {key: value + 5 for key, value in grades.items()}

print(grades)
# Output: {'Alice': 93, 'Bob': 97, 'Charlie': 80, 'Diana': 100}
5. Using pop() to Remove and Modify
If you want to remove an item from a dictionary and simultaneously update it or modify it, you can use pop().

Example:
python
Copy code
grades = {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95}

# Remove 'Bob' and modify Charlie's grade in one operation
removed_value = grades.pop('Bob', None)  # This will remove 'Bob'
grades['Charlie'] = 90  # Now modify Charlie's grade

print(grades)
# Output: {'Alice': 88, 'Charlie': 90, 'Diana': 95}
6. Using popitem() (for Random Removal)
You can use popitem() to remove and return a random key-value pair from the dictionary (in Python 3.7+, the removal is done in insertion order).

Example:
python
Copy code
grades = {'Alice': 88, 'Bob': 92, 'Charlie': 75, 'Diana': 95}

# Remove a random key-value pair
key, value = grades.popitem()
print(f"Removed {key}: {value}")

print(grades)
Summary of Methods:
Direct assignment (grades['Charlie'] = 90) is the simplest way to modify an existing key.
update() is useful for updating multiple keys at once.
setdefault() adds a key with a default value if the key doesn't exist, otherwise returns the current value.
Dictionary comprehension allows for bulk modifications or transformations.
pop() and popitem() can be used for removing and modifying values in one step.
'''
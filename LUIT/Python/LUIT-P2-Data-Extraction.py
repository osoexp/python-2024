'''
FOUNDATIONAL P2F
Create a script that generates a list of dictionaries about files in the working directory. Then print the list.
Push your code to GitHub and include the link in your write up.

ADVANCED P2A
Modify the script into a function such that any path can be passed as a parameter.  This parameter should be optional and should default to working directory when the variable is not passed. The function should then create the list of dictionaries about files from that path. The function should also return information on files nested in folders (recursive).

COMPLEX (Very Tricky) P2C
Modify the function to display recursive file information as dictionary of dictionaries.

'''

import os
from datetime import datetime

# Print a welcome message and prompt the user to select a level
print('Welcome To My Level Up In Tech Python Week 2 Project')
level_choice = int(input('Enter 1-3 to choose a level: \n \t  1. Foundational: \n \t  2. Advanced: \n \t  3. Complex: '))

def P2F():
    """Create a list of dictionaries containing file information in the current directory and print the list."""
    
    # List comprehension to gather file information for all files in the current directory
    files_info = [
        {
            'name': filename,  # Store the file name
            'size': os.path.getsize(filename),  # Store the file size in bytes
            'modified_time': datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S')  # Store the last modified time in a readable format
        }
        for filename in os.listdir('.') if os.path.isfile(filename)  # Only include files (not directories)
    ]
    
    # Print each dictionary in the list, each representing a file's information
    for info in files_info:
        print(info)

def P2A(path='.'):
    """Generate a list of dictionaries containing file information for the given path. Handles nested directories recursively."""
    
    # Initialize an empty list to store file information
    files_info = []

    def file_function(filepath):
        # Check if the path is a file
        if os.path.isfile(filepath):
            # Add file details to the list of file information
            files_info.append({
                'name': filepath,  # Store the full file path
                'size': os.path.getsize(filepath),  # Store the file size in bytes
                'modified_time': datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')  # Store the last modified time in a readable format
            })

    def dir_function(dirpath):
        # Iterate over items in the directory
        for item in os.listdir(dirpath):
            full_path = os.path.join(dirpath, item)  # Create the full path for the item
            file_function(full_path)  # Process the file
            if os.path.isdir(full_path):  # If the item is a directory, process it recursively
                dir_function(full_path)

    # Start processing from the given path (default is current directory)
    dir_function(path)
    
    # Print each file's information from the list
    for info in files_info:
        print(info)
    
    # Return the list of file information
    return files_info

def P2C(path='.'):
    """Display recursive file information as a dictionary of dictionaries."""
    
    def build_file_dict(dirpath):
        # Initialize an empty dictionary to store the directory's file information
        file_dict = {}
        
        # Iterate over items in the directory
        for item in os.listdir(dirpath):
            full_path = os.path.join(dirpath, item)  # Create the full path for the item
            
            if os.path.isfile(full_path):
                # Add file details to the dictionary
                file_dict[item] = {
                    'size': os.path.getsize(full_path),  # Store the file size in bytes
                    'modified_time': datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')  # Store the last modified time in a readable format
                }
            elif os.path.isdir(full_path):
                # If the item is a directory, recursively build its dictionary
                file_dict[item] = build_file_dict(full_path)
        
        # Return the dictionary representing the current directory's structure
        return file_dict

    # Build the dictionary of file structures starting from the given path (default is current directory)
    files_structure = build_file_dict(path)
    
    # Print the entire structure of files and directories
    print(files_structure)
    
    # Return the structure as a dictionary
    return files_structure

# Call the appropriate function based on the user's level choice
if level_choice == 1:
    P2F()
elif level_choice == 2:
    P2A()
elif level_choice == 3:
    P2C()
else:
    print('Choice Invalid. Exiting...')  # Handle invalid input


'''
OLD CODE 9/2/2024

print('Welcome To My Level Up In Tech Python Week 2 Project')
level_choice = int(input('Enter 1-3 to choose a level: \n \t  1. Foundational: \n \t  2. Advanced: \n \t  3. Complex: '))

def P2F():
    import os
    from datetime import datetime

    # List to store file information dictionaries
    files_info = []

    # Loop through each item in the current directory
    for filename in os.listdir('.'):

        # Check if the item is a file (not a directory)
        if os.path.isfile(filename):

            # Create a dictionary with file details
            file_info = {
                'name': filename,
                'size': os.path.getsize(filename),  # Get the file size in bytes
                'modified_time': datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S')  # Get the last modified time
            }

            # Add the file info dictionary to the list
            files_info.append(file_info)

    # Print the list of file information
    for i in files_info:
        print(i)


def P2A():   
    import os
    import sys
    from datetime import datetime

    # Check if at least one argument is passed
    if len(sys.argv) > 1:
        # Get the first argument (excluding the script name)
        user_argument = str(sys.argv[1]).strip()
        print(f"We will use the path: {user_argument}")
    else:
        print("No arguments passed. Using current working directory \n")

        # List to store file information dictionaries
        files_info = []

        def file_function(i):
            if os.path.isfile(i):
                # Create a dictionary with file details
                file_info = {
                    'name': i,
                    'size': os.path.getsize(i),  # Get the file size in bytes
                    'modified_time': datetime.fromtimestamp(os.path.getmtime(i)).strftime('%Y-%m-%d %H:%M:%S')  # Get the last modified time
                }
                # Add the file info dictionary to the list
                files_info.append(file_info)

        def dir_function(j):
            if os.path.isdir(j):
                for dir_name in os.listdir(j):
                    full_path = os.path.join(j, dir_name)  # Construct full path
                    file_function(full_path)
                    if os.path.isdir(full_path):  # Corrected to os.path.isdir
                        dir_function(full_path)  # Recursive call with the full path

        # Loop through each item in the current directory
        for filename in os.listdir('.'):
            full_path = os.path.join('.', filename)  # Construct full path
            file_function(full_path)
            dir_function(full_path)
        
        for element in files_info:
            print(element)
        return files_info

        
# Call the function and print the result
# print(P2C())


def P2C():
    import os
    from datetime import datetime




if level_choice == 1:
    P2F()
elif level_choice == 2:
    P2A()
elif level_choice == 3:
    P2C()
else:
    print('Choice Invalid. Exiting...')
'''
import os
from datetime import datetime

'''
> The value '.' is passed to os.listdir() because it is shorthand for the current working directory.
> os.path.isfile is performing a check. So it will return true or false.
> We create a dictionary entries
> As we are creating dictionary entries we get the modified time from the file. Then transform it using datetime. 
>.strftime then takes the human readable values and formats them.
> Then we append it to file_info

'''

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
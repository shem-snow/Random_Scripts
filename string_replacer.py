'''
Use this script specify a filepath, an old string, and a new string.
When the script is run, the specified file will be opened and all instances of "old_string"
will be replaced with "new_string".
'''

file_path = "file.ext"  # Replace with the path to your text file
old_string = "pirntf"
new_string = "printf"

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Replace the old string with the new one.
updated_content = file_content.replace("pirntf", "printf")

# Write the updated content back to the file
with open(file_path, 'w') as file:
    file.write(updated_content)

print("Replacement complete.")
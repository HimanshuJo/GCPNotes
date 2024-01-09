import os

# Define the folder name and path
folder_name = "ACE_Questions"
folder_path = os.path.join(os.getcwd(), folder_name)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create 255 files inside the folder
for i in range(1, 256):
    # Format the file name with leading zeros
    file_name = f"{i:03d}_Question.txt"
    file_path = os.path.join(folder_path, file_name)

    # Create and write to the file
    with open(file_path, 'w') as file:
        file.write(f"This is question {i}.")

print(f"Folder '{folder_name}' and files created successfully.")
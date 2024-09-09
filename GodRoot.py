import os

def list_files_in_folder(folder_path):
    try:
        # Get a list of all files and directories in the specified folder
        files_and_dirs = os.listdir(folder_path)
        
        # Filter out directories and keep only files
        files = [f for f in files_and_dirs if os.path.isfile(os.path.join(folder_path, f))]
        
        return files
    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
        return []
    except PermissionError:
        print(f"Permission denied to access the folder '{folder_path}'.")
        return []

# Example usage
folder_path = "C:/Users/vk200/OneDrive/Pictures/SIH-Hackthon-project/HPmain/media"

# Get the list of files
files = list_files_in_folder(folder_path)

# Print the result
print(files)

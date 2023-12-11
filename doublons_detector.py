from pathlib import Path
import os
import hashlib
from tqdm import tqdm  # Import tqdm for the progress bar

# Project Directory
DIR_FILE = Path(__file__).resolve()
DIR_PATH = DIR_FILE.parent

# Dir manipulation
class ReadDir:
    def __init__(self, dir_name) -> None:
        self.folder_search = dir_name

    # Read directory 
    def read_dir(self):
        search_exist = os.path.exists(self.folder_search)

        try:
            if search_exist:
                print(f"Folder {self.folder_search} Exist")
                return 1
            else:
                print(f"Folder {self.folder_search} doesn't exist")
                return 0
        except Exception as e:
            print(f"Exception code: 102 - {e}")

    # Search all doublons in the path and the sub path
    def search_doublons(self):
        try:
            if self.read_dir() == 1:
                dir_folder = Path(self.folder_search)

                # Use os.walk to list all files in the directory and its subdirectories
                all_files = [os.path.join(root, file) for root, dirs, files in os.walk(dir_folder) for file in files]

                # Use a dictionary to identify duplicate files based on their content
                file_dict = {}
                duplicate_files = []

                # Use tqdm to display a progress bar with a green color
                for file_path in tqdm(all_files, desc="Checking duplicates", unit="file"):
                    with open(file_path, 'rb') as f:
                        file_content = f.read()
                        file_hash = hashlib.md5(file_content).hexdigest()

                    if file_hash not in file_dict:
                        file_dict[file_hash] = file_path
                    else:
                        duplicate_files.append((file_path, file_dict[file_hash]))

                return duplicate_files
            elif self.read_dir() == 0:
                return []
        except Exception as e:
            print(f"Error code: 101 - {e}")

# Save to the list
def save_list(list_doublons):
    file_name = "list.txt"

    with open(file_name, 'w', encoding="UTF-8") as file:
        for item in list_doublons:
            file.write(f"Duplicate File 1: {item[0]}\nDuplicate File 2: {item[1]}\n\n")

# Main menu
if __name__ == "__main__":
    my_dir = input(f"Please write your path: ")

    read = ReadDir(my_dir)
    
    list_doublons = read.search_doublons()
    save_list(list_doublons=list_doublons)

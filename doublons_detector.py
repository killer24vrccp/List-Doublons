from pathlib import Path
import os

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
                return os.listdir(dir_folder)
            elif self.read_dir() == 0:
                return []
        except Exception as e:
            print(f"Error code: 101 - {e}")

# Save to the list
def save_list(list_doublons):
    file_name = "list.txt"

    with open(file_name, 'w', encoding="UTF-8") as file:
        for item in list_doublons:
            file.write(f"{item}\n")

# Main menu
if __name__ == "__main__":
    my_dir = input(f"Please write your path: ")

    read = ReadDir(my_dir)
    
    list_doublons = read.search_doublons()
    save_list(list_doublons=list_doublons)

import os

file_path = "/Users/David/Projects/Udacity-Python/prank/"

def rename_files():
    file_list = os.listdir(file_path)
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(file_path)

    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()

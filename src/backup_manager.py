import os
import shutil

# Get source folder and create a safe copy with _organized suffix
def create_safe_backup(source_folder):

    # check if the source folder exists
    if not os.path.exists(source_folder):
        print("Error: The desired folder was not found!")
        return None

    # get the absolute path of the folder
    full_path = os.path.abspath(source_folder)

    # create new folder path with _organized suffix
    destination_folder = full_path + "_organized"

    # delete old organized folder if it already exists
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)


    # copy everything from source to destination
    shutil.copytree(full_path, destination_folder)


    # return the new folder path
    return destination_folder


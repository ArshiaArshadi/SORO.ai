import os
import shutil
import file_utils

# define extension categories map
Ex_Map = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
}

# Accept target folder and group all files by extension
def filter_by_extension(target_folder):

    # get all files and folders inside target directory
    all_items = os.listdir(target_folder)

    for item in all_items:
        # create full path for each item
        item_path = os.path.join(target_folder, item)

        # check if item is a file
        if os.path.isfile(item_path):
            # get file extension
            ext = file_utils.get_file_extension(item_path)

            moved = False  # file movement status flag

            # loop through defined extension categories
            for folder_name, extensions_list in Ex_Map.items():
                if ext in extensions_list:
                    new_folder_path = os.path.join(target_folder, folder_name)

                    # create category folder if it does not exist
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)

                    shutil.move(item_path, new_folder_path)
                    moved = True
                    break

            # move unknown extensions to Others folder
            if not moved:
                others_path = os.path.join(target_folder, "Others")
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(item_path, others_path)



# Accept target folder and isolate files larger than size limit
def filter_by_size(target_folder, size_limit_mb=10):


    all_items = os.listdir(target_folder)

    for item in all_items:
        item_path = os.path.join(target_folder, item)

        if os.path.isfile(item_path):
            # get file size in megabytes
            file_size = file_utils.get_file_size_mb(item_path)

            # check if file size is greater than limit
            if file_size > size_limit_mb:
                heavy_folder_path = os.path.join(target_folder, "Heavy_Files")
                
                if not os.path.exists(heavy_folder_path):
                    os.makedirs(heavy_folder_path)

                shutil.move(item_path, heavy_folder_path)



# Accept target folder and organize files by year and month
def filter_by_timeline(target_folder):


    all_items = os.listdir(target_folder)

    for item in all_items:
        item_path = os.path.join(target_folder, item)

        if os.path.isfile(item_path):
            # get year and month
            year, month = file_utils.get_file_creation_date(item_path)

            # create archive nested folder path
            archive_path = os.path.join(
                target_folder, "Timeline_Archive", year, month
            )

            
            if not os.path.exists(archive_path):
                os.makedirs(archive_path)

            shutil.move(item_path, archive_path)


from datetime import datetime
import os


# Accept file path and return extension in lowercase
def get_file_extension(file_path):
    # split file into name and extension
    _, extension = os.path.splitext(file_path)
    # return extension in lowercase
    return extension.lower()


# Accept file path and calculate size in megabytes
def get_file_size_mb(file_path):
    # get file size in bytes
    bytes_size = os.path.getsize(file_path)
    # convert bytes to megabytes
    megabytes_size = bytes_size / (1024 * 1024)
    return megabytes_size


# Accept file path and get modified year and month
def get_file_creation_date(file_path):
    # get raw modification timestamp from system
    timestamp = os.path.getmtime(file_path)

    # convert timestamp to readable date object
    date_object = datetime.fromtimestamp(timestamp)

    # extract year and month
    year = date_object.strftime("%Y")
    month = date_object.strftime("%m-%B")

    return year, month
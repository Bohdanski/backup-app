"""
Scheduled script for backing up local files to network drive.
"""

import time
import datetime
from os import path
from shutil import make_archive

def compress(src_path, dest_path, folders):
    """
    Take in an array of folders to compress and save to
    a specified location. Generates a log file containing
    runtime information.
    """
    output_file = open(dest_path + "log.txt", "w+")
    timestamp = datetime.datetime.now()
    start_time = time.time()

    for folder in folders:
        folder_path = src_path + folder

        if path.exists(folder_path):
            make_archive(f"{dest_path}Backup-{folder}", "zip", folder_path)
            output_file.write(f"'{folder_path}' compressed successfully\n")
        else:
            output_file.write(f"WARNING: Directory not found: '{(folder_path)}'\n")

    output_file.write(f"\nScript execution timestamp: {str(timestamp)}\n")
    output_file.write(f"Script runtime: {time.time() - start_time} seconds\n")
    output_file.close()

def main():
    """
    Main function where all logic is executed, folders
    to be backed up are declared here as well as any
    working directories.
    """
    folders = ["2020", "MicroStrategy", "Nielsen", "Projects", "Python", "SQL", "Visual Basic"]

    src_path = "C:\\Users\\tubxt2p\\Documents\\"
    dest_path = "Q:\\"

    compress(src_path, dest_path, folders)

if __name__ == "__main__":
    main()

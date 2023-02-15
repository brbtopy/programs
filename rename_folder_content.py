#!/usr/bin/env python3
import os

# SORTS CONTENTS OF DIRECTORY BY CREATION DATE THEN RENAMES TO STRING OF CHOICE
def rename_files_in_directory(directory):
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(directory, x)), os.listdir(directory))
    list_of_files = sorted(list_of_files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))

    for count, filename in enumerate(list_of_files):
        count += 1
        dst = f"notes {str(count)}"             # 'notes' is the demo name all the files will begin with
        src = f"{directory}/{filename}"
        dst = f"{directory}/{dst}"
        # print("Renaming " + src + " --- > " + dst)

        os.rename(src, dst)

directory = "/root/test"        # LINUX DIRECTORY OF FOLDER CONTAINING FILES. USE CORRECT SYNTAX FOR OTHER OPERATING SYSTEMS
rename_files_in_directory(directory)

# OUTPUT WOULD LOOK LIKE THE FOLLOWING SINCE dst VARIABLE USES 'notes'
# notes 1
# notes 2
# notes 3
# notes 4

import os
import shutil
from .config import CHROME_DEV_DATA_PATH, BACKUP_PATH


def restore_onetab(index: int) -> None:
    """Restore OneTab data.

    Args:
        index (int): Index of the backup with 0 being the latest and 1 being the second latest.

    Returns:
        None
    """
    # define dest directory
    dest = CHROME_DEV_DATA_PATH

    # define src directory
    backups = next(os.walk(BACKUP_PATH))[1]
    backups.reverse()
    src = BACKUP_PATH + backups[index] + "/leveldb"

    # getting file numbers from src
    src_files = os.listdir(src)
    src_files_compare = [file_name for file_name in src_files]

    # remove files not in src from dest
    print("removing files not in " + src + " from " + dest)
    dest_files = os.listdir(dest)
    for file_name in dest_files:
        if file_name == "LOCK":
            continue
        full_file_name = os.path.join(dest, file_name)
        if os.path.isfile(full_file_name) and file_name not in src_files_compare:
            os.remove(full_file_name)
            print("deleted " + file_name)

    # copy ldb and log files from local directory to chromedata directory
    print("copying from " + src + " to " + dest)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
            print("copied " + file_name)

    print("restore complete\n")

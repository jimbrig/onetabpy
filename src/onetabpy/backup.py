import os
import shutil
from datetime import datetime

from .utils.browsers import ChromeEdition
from .config import CHROME_DATA_PATH, CHROME_DEV_DATA_PATH, BACKUP_PATH, EXCLUDES


def backup_onetab(edition: ChromeEdition = ChromeEdition.CHROME) -> None:
    """Backup OneTab data.

    Args:
        edition (ChromeEdition, optional): Chrome edition. Defaults to ChromeEdition.CHROME.

    Returns:
        None
    """
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    print("date and time:", date_time)

    src = ""

    if edition == ChromeEdition.CHROME:
        src = CHROME_DATA_PATH
    elif edition == ChromeEdition.CHROME_DEV:
        src = CHROME_DEV_DATA_PATH

    dest_parent = BACKUP_PATH + date_time
    os.mkdir(dest_parent)
    print(dest_parent + " created")
    dest = dest_parent + "/leveldb"
    os.mkdir(dest)
    print(dest + " created")

    print("copying from " + src + " to " + dest)
    src_files = os.listdir(src)
    for file_name in src_files:
        if file_name in EXCLUDES:
            continue
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
            print("copied " + file_name)

    print("backup complete\n")

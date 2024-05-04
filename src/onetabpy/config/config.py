import os

HOME_PATH = os.path.expanduser("~")
CONFIG_PATH = HOME_PATH + "/.config/"
LOCALAPPDATA_PATH = os.getenv("LOCALAPPDATA")

CHROME_DATA_PATH = (
    LOCALAPPDATA_PATH + "/Google/Chrome/User Data/Default/Local Storage/leveldb"
)
CHROME_DEV_DATA_PATH = (
    LOCALAPPDATA_PATH + "/Google/Chrome Dev/User Data/Default/Local Storage/leveldb"
)
CHROME_BETA_DATA_PATH = (
    LOCALAPPDATA_PATH + "/Google/Chrome Beta/User Data/Default/Local Storage/leveldb"
)

BACKUP_PATH = CONFIG_PATH + "onetab/"

EXCLUDES = ["LOCK"]

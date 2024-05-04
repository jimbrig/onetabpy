import sys

from onetabpy.backup import backup_onetab
from onetabpy.restore import restore_onetab
from onetabpy.cli import main as cli


def cli_main():
    """Entry point for the CLI."""
    cli.onetabpy()


def main():
    """Main function."""
    args = sys.argv[1:]
    print()
    if len(args) == 0:  # no args are input
        fn = input("Backup or restore? ").lower()
        print()
        if fn == "backup":
            backup_onetab()
        elif fn == "restore":
            index = int(input("Enter the backup ID: "))
            restore_onetab(index)
        else:
            print("Error: Function not found")
        print(input("Press 'Enter' to exit"))
    elif len(args) > 0 and args[0] == "--backup":  # '--backup' arg is input
        backup_onetab()
    elif len(args) > 0 and args[0] == "--restore":  # '--restore <int>' args are input
        index = int(args[1])
        restore_onetab(index)

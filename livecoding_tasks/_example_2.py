from pathlib import Path
from tempfile import TemporaryDirectory
import time
import os


current_folder = os.getcwd()
name_folder = "Temp"

print(current_folder)


def new_method():
    with TemporaryDirectory(dir=current_folder) as db_dir:
        print(db_dir)
        time.sleep(10)


new_method()

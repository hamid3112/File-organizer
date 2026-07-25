#import moduls and global variable
from pathlib import Path
import shutil

base_directory =Path( r"C:\Users\iTop_Store\Downloads")
target_directory = base_directory /'sorted'

#defin categoris and extentions
FILE_CATEGORIES = {

    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],

    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],

    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],

    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],

    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"]    

}

#craeating directory for categoris
def creating_categoris_directory ():
    for categories,_ in FILE_CATEGORIES.items():
        (target_directory / categories).mkdir(parents=True , exist_ok=True)

#searching and categories file
def searching_and_categories ():
    for file in base_directory.rglob("*"):
        if target_directory in file.parents:
            continue
        for categories , extention in FILE_CATEGORIES.items():
            if file.suffix in extention :
                file.copy_into( target_directory / categories , preserve_metadata=True)
#run app
creating_categoris_directory()
searching_and_categories()
import os, shutil
from pathlib import Path

print("Current dir is: ", os. getcwd())

os.chdir('C:\\DOC\\OrganizeMe')

print("Now I'm in: ", os. getcwd())
# backup testing directory
shutil.copytree('C:\\DOC\\OrganizeMe', 'C:\\DOC\\OrganizeMe_')

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def pickDirectory(name):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == name:
                return category
    return 'MISC' #If filetype doesn't exist in our dictionary

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()

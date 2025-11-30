import os
import shutil
import time

cwd = os.chdir('C:/Users/USER/Downloads')

# available extentions for the files
image_exts = [
    ".png", 
    ".jpg", 
    ".webp", 
]

app_exts = [
    ".exe",
    ".msi",
]

video_exts = [
    ".mp4", 
    ".webm", 
    ".avi",
]

audio_exts = [
    #why is there so many
    ".wav",
    ".mp3",
    ".ogg",
    ".flac",
    ".wma",
    ".aac",
    ".m4a",
    ".m4b",
    ".aiff",

]

doc_exts = [
    ".pdf", 
    ".epub", 
    ".mobi", 
    ".txt",
    ".odt",
    ".rtf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ]

zipped_exts = [
    ".zip",
    ".7z",
    ".rar",
]

folder_names = [
    "Images", 
    "Videos", 
    "Apps", 
    "Zipped Files", 
    "Audio", 
    "Documents", 
]
files = os.listdir(cwd)

# Asks whether or not to create the folders and is the start of the program
def foldersconfirm():
    os.system('cls' if os.name == 'nt' else 'clear')
    folder_confirmation = input("Create Folders [y/n]:")
    if folder_confirmation == "y" or folder_confirmation == 'Y':
        createfolders()
    elif folder_confirmation == "n" or folder_confirmation == 'N':
        currentpath()
        getfiles()
        movefiles()
    else:
        foldersconfirm()

# Lists current path thats being used 
def currentpath():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print("-" * 30)
    print("Current Directory: " + os.getcwd())
    print("-" * 30)
    print()
# Just prints out a list of the files for aesthetic purposes i guess
def getfiles():
    #get list of files
    for i in range(0, len(files)):
        print(files[i])
        i += 1
    print()
# Creates the folders to put the files in
def createfolders():
    for i in range(0, len(folder_names)):
        try:
            os.mkdir(folder_names[i])
            i += 1
            if i == len(folder_names):
                print("Folders Created.")
        except:
            print("Folder " + folder_names[i] + " already exists.")
            i += 1
    time.sleep(2)
    currentpath()
    getfiles()
    movefiles()

# Moves the files to the created folders
# If its any other filetype than the ones in file_exts, it ignores it
# with this aproach it makes it difficult to make an "others" folder since it can put the rest of the folders in that folder
def movefiles():
    moveconfirm = input("Move files to folders?: [y/n]:")
    if moveconfirm == "y" or moveconfirm == 'Y':
        for i in range(0, len(files)):
            filename, filetype = os.path.splitext(files[i])
            print("Moving "+ files[i])
            if filetype in image_exts:
                shutil.move(files[i], "./Images")
            elif filetype in app_exts:
                shutil.move(files[i], "./Apps")
            elif filetype in video_exts:
                shutil.move(files[i], "./Videos")
            elif filetype in audio_exts:
                shutil.move(files[i], "./Audio")
            elif filetype in doc_exts:
                shutil.move(files[i], "./Documents")
            elif filetype in zipped_exts:
                shutil.move(files[i],"./Zipped Files")
            else:
                print("Could not move " + files[i])
                pass
        print("Actions Done.")
        time.sleep(2) # <<< not sure why i used these, maybe since i liked to see the window, but you can erase these
    elif moveconfirm == "n" or moveconfirm == 'N': 
        print("No Actions Done.")
        time.sleep(2)
    else:
        movefiles()


foldersconfirm()

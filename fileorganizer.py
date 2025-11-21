import os
import shutil
import time

cwd = os.chdir('C:/Users/user/Downloads')

# available extentions for the files
file_exts = [
    ".png", # index 0
    ".jpg", # index 1
    ".webp", # index 2
    ".exe", # index 3
    ".mp4", # index 4
    ".webm", # index 5
    ".mp3", # index 6
    ".wav", # index 7
    ".pdf", # index 8
    ".epub", # index 9
    ".mobi", # index 10
    ".zip", # index 11
]

folder_names = [
    "Images", # index 0
    "Videos", # index 1
    "Apps", # index 2
    "Files", # index 3
    "Audio", # index 4
    "Documents", # index 5
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
            if filetype in file_exts[:3]:
                shutil.move(files[i], "./Images")
            elif filetype == file_exts[3]:
                shutil.move(files[i], "./Apps")
            elif filetype in file_exts[4:6]:
                shutil.move(files[i], "./Videos")
            elif filetype in file_exts[6:8]:
                shutil.move(files[i], "./Audio")
            elif filetype in file_exts[8:11]:
                shutil.move(files[i], "./Documents")
            elif filetype == file_exts[11]:
                shutil.move(files[i],"./Files")
            else:
                pass
        print("Actions Done.")
        time.sleep(2) #not sure why i used these, maybe since i liked to see the window, but you can erase these
    elif moveconfirm == "n" or moveconfirm == 'N': 
        print("No Actions Done.")
        time.sleep(2)
    else:
        movefiles()


foldersconfirm()

import os
import shutil

#INITIALIZE FOLDER EXTENSIONS
audios = ['mp3', 'wav', 'flac', 'midi', 'wma', 'aac', 'm4a']
videos = ['mp4', 'avi', 'mov', 'wmv', 'mkv', 'flv', 'mpeg', '3gp']
images = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", 'tif']
docs = ["doc", "docx", "pdf", "txt", "ppt", "pptx", "xls", "xlsx"]
executables = ["exe", "bat", "sh", "app", "jar", 'iso']
comp = ["zip", "rar", "7z", "tar", "gz", "bz2", "xz"]
scripts = ['py', 'c', 'js', 'css', 'java', 'jsx', 'rb', 'php', 'swift', 'ts', 'go', 'rs', 'kt', 'scala', 'pl']

homePath = os.path.expanduser('~')
basePath = os.path.join(homePath, 'Downloads')
destPath = ['Audios', 'Videos', 'Pictures', 'Documents', 'Executables', 'Compressed Files', 'Program Code', 'Random']

#CREATE FOLDERS
for dir in destPath:
    dirPath = os.path.join(basePath, dir)

    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)

fileList = os.listdir(basePath)

#MOVE TO CREATED FOLDERS
for file in fileList:
    fileExt = file.split(".")[-1]

    if fileExt in images:
        shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Pictures/"))
    elif fileExt in docs:
        shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Documents/"))
    elif fileExt in audios:
        shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Audios/"))
    elif fileExt in videos:
        shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Videos/"))
    elif fileExt in executables:
        shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Executables/"))
    elif fileExt in comp:
        shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Compressed Files/"))
    elif fileExt in scripts:
        shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Program Code/"))
    else:
        if file.split(".")[0] not in destPath:
            tempPath = os.path.join(os.path.join(basePath, file))
            if os.path.isdir(tempPath):
                All = True

                for file2 in os.listdir(tempPath):
                    if file2.split(".")[-1] not in images:
                        All = False
                        break

                if All:
                    shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Pictures/"))
                else:
                    shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Random/"))
            else:
                    shutil.move(os.path.join(basePath, file), os.path.join(basePath, "Random/"))

print('Done')
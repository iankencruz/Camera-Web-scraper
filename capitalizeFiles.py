import os


#! Make sure to set directory
#TODO Make it ask for directory to os.walk
directory = r'E:\Anime'

#* Walk Through Directory

for rootFolder, folderName, fileName in os.walk(directory):
    print("root = " + rootFolder)

    #* Get Details of all folders inside working directory
    for folders in folderName: 
        print('Foldernames = ' + folders)
        names = folders
        capName = names.capitalize()
        print ('cap: ' + capName)

        #* Rename and better format (strip) 
        try:
            oldName = '{}\{}'.format(rootFolder, names)
            newName = '{}\{}'.format(rootFolder, capName)
            newName.strip()
            os.rename(oldName, newName)
            print('renamed')

        except FileNotFoundError:
            print("ERROR: Name does not match")                    #*Error check

        

    print (' ')





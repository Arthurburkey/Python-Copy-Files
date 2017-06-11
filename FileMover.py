##Arthur A. Burkey III
##Title: File Mover – Python 2.7 – IDLE
##Scenario: Your employer wants a program to move all his .txt files from one folder to another
##with the click of a click of a button. On your desktop make 2 new folders. Call one Folder A &
##the second Folder B. Create 4 random .txt files & put them in Folder A.
##Plan:
##- Move the files from Folder A to Folder B.
##- Print out each file path that got moved onto the shell.
##- Upon viewing Folder A after the execution, the moved files should not be there.
##Guidelines:
##● Use Python 2.7 .x on this drill.
##● Import the shutil module.
##● Run it on the python shell.
##● Use the IDLE for this Drill

import shutil
import os, sys

##def cp():
##    
##    shutil.copy('textFile1.txt', '\A\B')
##    shutil.copy('textFile2.txt', '\A\B')
##    shutil.copy('textFile3.txt', '\A\B')
    


src = "C:\Users\Student\Desktop\A"
dst = "C:\Users\Student\Desktop\A\B"
prntSrc = os.listdir(src)
prntDst = os.listdir(dst)
print 'BEFORE copy operation: '
print(prntDst)

def fileCopy():
    
    print(prntSrc)
    for files in prntSrc:
        if files.endswith(".txt"):
            print (files)
            shutil.copy(files, dst)
    print 'AFTER copy operation: '
    print ''
    print 'Destination Dir after copy operation: '
    prntDst = os.listdir(dst)
    print(prntDst)
fileCopy()


##https://docs.python.org/2/library/shutil.html
## shutil.copyfile( src, dest )
##https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python

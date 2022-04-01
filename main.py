import os
import shutil
import time
path = input('Enter the path for removing the files')
files = os.listdir(path)
now = time.time()
print(now)
for i in files:
    ctime = os.stat(path + '/'+i).st_ctime
    diff = now-ctime
    daysinsec = 30*24*60*60
    fileName, fileExt = os.path.splitext(i)
    if diff > daysinsec:
        if fileExt != "":
            os.remove(path+'/'+i)
        else:
            shutil.rmtree(path+'/'+i)

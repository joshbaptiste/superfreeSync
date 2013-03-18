#!/usr/bin/env python3

import os 
#import inotify

#on startup scan src dir if exists
#scan cache dir 
SRC_DIR = {}
SRC_DIR['/superfree'] = ['movies','tv_series']
#CACHE_DIR = '/superfree-cache'
CACHE_DIR = '/home/junya'
TIME_IN_DAYS = 30

def scanDirectories():
    sourceDir = SRC_DIR.keys()[0]
    for root, dirs, files in os.walk(CACHE_DIR):
        dirs[:] = SRC_DIR['/superfree']
        #skip hidden directories
        dirs[:] = [d for d in dirs if not d[0] == '.']
        if os.path.exists(root.replace(sourceDir,CACHE_DIR,1))
            pass
            print('exists')
        else:
            if os.path.isfile(root):
                f = os.stat(root)
                f.st_atime(root) > TIME_IN_DAYS * 86400
            rsyncFile(sourceDir,CACHE_DIR)

        print(root)
         
        


if __name__ == "__main__":
    scanDirectories()
    #inotify wait here..

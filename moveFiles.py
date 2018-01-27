import shutil
import os
import time
import glob

path = os.getcwd()
directory = path + os.path.join('\\DEAR_import\\')
dir_dst = directory + '\\DEAR_Archive\\'
timestr = time.strftime("%Y%m%d-%H%M%S")

def moveFiles():
	for filename in os.listdir(directory):
	    if filename.endswith('.csv'):
	        shutil.move( directory + filename, dir_dst)

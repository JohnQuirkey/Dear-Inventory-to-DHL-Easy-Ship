import shutil
import os
import time
import glob

path = os.getcwd()
directory = path + os.path.join('\\PATH_TO_DHL_FOLDER\\')
dir_dst = directory + '\\MAKE_SURE_THIS_FOLDER_EXISTS_IN_THE_DEAR_FOLDER\\'
timestr = time.strftime("%Y%m%d-%H%M%S")

def moveFiles():
	for filename in os.listdir(directory):
	    if filename.endswith('.csv'):
	        shutil.move( directory + filename, dir_dst)

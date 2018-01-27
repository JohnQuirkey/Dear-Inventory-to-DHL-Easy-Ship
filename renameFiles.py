import os
import shutil
import time


path = os.getcwd()
arch_src = path + '\\DEAR_import\\DEAR_Archive\\'
timestr = time.strftime("%Y%m%d-%H%M%S")

print("**************************************")
print("* DEAR Invoice extraction            *")
print("* Pestle & Mortar 2018               *")
print("* JQuirke                            *")
print("**************************************")
print(" ")

def renameFile():
    for filename in os.listdir(arch_src):
        if filename.endswith('.csv'):

            print("File procesed --> " + filename)
            print(" ")


            shutil.move(arch_src + filename, arch_src + timestr +'_'+ filename + '_ARCHIVED')

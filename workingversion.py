import os
import zipfile
from zipfile import ZipFile
from shutil import copyfile
from datetime import date
import shutil
import subprocess 

Home = 'C:\\Users\\Clement Familusi\\Dropbox (VirtualClarity)\\Clement F'
currentDate = format(date.today())
unpackedFile = 'UNPKD'


      #Copy all .pbix files (date them), zip up the dated copies
for file in os.listdir(Home):
    if file.endswith(".pbix"):
      print(os.path.join(file))
      shutil.copy(os.path.join(Home, file), os.path.join(Home, file + ' ' + currentDate + '.zip'))
      
      #Extract the files from those zips   
for file in os.listdir(Home):
    if file.endswith(".zip"):
      print(os.path.join(file))
      zip = ZipFile(file)
      zip.extractall(unpackedFile)
      
#for file in os.listdir('C:\\Users\\Clement Familusi\\Dropbox (VirtualClarity)\\Clement F\\UNPKD'):
 #   if file.endswith("DataMashup"):
  #    print(os.path.join(file))

      

print('...DONE')      
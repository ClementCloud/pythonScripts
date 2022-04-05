import os
import zipfile
from zipfile import ZipFile
from shutil import copyfile
from datetime import date
import shutil

Home = 'C:\\Users\\Clement Familusi\\Dropbox (VirtualClarity)\\Clement F'
currentDate = format(date.today())
unpackedFile = 'UNPKD'

      #Copy all .pbix files (date them), zip up the dated copies
for file in os.listdir(Home):
    if file.endswith(".pbix"):
    	print(os.path.join(file))
    	shutil.copy(os.path.join(Home, file), os.path.join(Home, file + '' + currentDate + '.zip'))
      
      #Extract the files from those zips   
for file in os.listdir(Home):
    if file.endswith(".zip"):
      print(os.path.join(file))
      zip =ZipFile(file)
      zip.extractall(unpackedFile)


      #Copy and .7zip the copies of the unpacked files
for file in os.listdir(unpackedFile):
    print(os.path.join(file))
    shutil.copy(os.path.join(unpackedFile, file), os.path.join(unpackedFile, file + '' + currentDate + '.7zip'))

    #Unpack the .7zip files
for file in os.listdir(unpackedFile):
    if file.endswith(".7zip"):
      print(os.path.join(file))
      zip =ZipFile(file)
      zip.extractall(unpackedFile)

    #Open a destination file, locate all of the unpacked .7zip files that are typ .m
f1 = open('dst.txt', 'w+')        
for file in os.listdir(unpackedFile):
    if file.endswith(".m"):
    print(os.path.join(file))
    
    #Open the .m files, read them and print the relevant data to the destination file
      with open(file, 'r') as s:
      for line in s:
        ftext = s.readline()
        wrd1 = 'Source = '
        res = ftext.partition(wrd1)[2] 
        wrd2 = 'Item='
        res1 = ftext.partition(wrd2)[2] 
        f1.write(res + res1)
        print(res + res1) 

s.close()
f1.close()
    


    #print(os.path.join(file))
    #shutil.copy(os.path.join(unpackedFile, file), os.path.join(unpackedFile, file + currentDate + '.7zip'))









#orgName = 'Application Passport'
#mainFile = orgName + '.pbix'
#newFile = orgName + currentDate + '.zip'
#copyfile(mainFile, newFile)
	#OPEN THE NEW FILE AND TURN ALL OF ITS FILES TO .7zip

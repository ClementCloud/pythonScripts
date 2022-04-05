import os
import zipfile
from zipfile import ZipFile
from shutil import copyfile
from datetime import date
import shutil

Home = 'C:\\Users\\Clement Familusi\\Dropbox (VirtualClarity)\\Clement F'
currentDate = format(date.today())

#TURN FILE INTO A ZIP
	#CREATE A NEW FILE FOR ALL .pbix FILES
for file in os.listdir(Home):
    if file.endswith(".pbix"):
    	print(os.path.join(file))
    	shutil.copy(os.path.join(Home, file), os.path.join(Home, file + currentDate + '.zip'))
    if file.endswith('.zip'):
		shutil.unpack_archive(file, file + 'Unpked')









#orgName = 'Application Passport'
#mainFile = orgName + '.pbix'
#newFile = orgName + currentDate + '.zip'
#copyfile(mainFile, newFile)
	#OPEN THE NEW FILE AND TURN ALL OF ITS FILES TO .7zip

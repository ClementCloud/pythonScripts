import re
import os
from zipfile import ZipFile
import pyodbc 
from datetime import datetime
import zipfile
from shutil import copyfile
from datetime import date
import shutil
import subprocess 
from io import BytesIO

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))
saved_database = ''
saved_server = ''
reportName = ''
reportFolder = ''
Home = 'C:\\Users\\Clement Familusi'
Dest = Home + '\\PBIX'
file1 = 'dst.txt'
currentDate = format(date.today())

conn = pyodbc.connect('Driver={SQL Server};'
            'Server=LAPTOP-FRP9CFGL;'
            'Database=dec;'
            'Trusted_Connection=yes;')


def main():
    #copyPBIXFiles(Home + '\\Documents\\GitHub\\powerbi-reports')
    #pullPBIXFiles(Dest)
    extract_section_1_m('Wave Schedule.pbix', 'dst.txt')

def copyPBIXFiles(dir):
    fileNames= os.walk(dir)
    for root, dirs, files in fileNames:
        for file in files:
            try:
                if file.endswith(".pbix"):
                    g = str(os.path.join(root,file))
                    print(g)
                    gg =str(file)
                    shutil.copy(os.path.join(root, file), os.path.join(Dest, file))
                    #pullPBIXFiles(dir)
            except shutil.SameFileError:
                print(file + ' already exists in the folder')
      
def pullPBIXFiles(dir):
    global reportName, reportFolder
    fileNames= os.walk(dir)
    for root, dirs, files in fileNames:
        for file in files:
            if file.endswith(".pbix"):
                g = str(os.path.join(root,file))
                print(g)
                gg =str(file)
                reportFolder = str(root)
                reportName = str(file)
                extract_section_1_m(g, file1)
      




def extract_section_1_m(pbix_filename, destination):
    with zipfile.ZipFile(pbix_filename, 'r') as pbx_file:
        try:
            with pbx_file.open('DataMashup') as dm:
                contents = dm.read()
                package_part_length = int.from_bytes(contents[4:8], byteorder='little')
                zip_binary = contents[8: 8 + package_part_length]
                zip_memory_file = BytesIO(zip_binary)    
                with zipfile.ZipFile(zip_memory_file) as z:
                    contents = z.read('Formulas/Section1.m')
                    with open(destination, 'w') as s:
                        s.write(str(contents, 'utf-8'))
                        s.flush()
                        s.close()
                        process_file(file1)
        except (KeyError):
            print ('DataMashup does not exist in ' + pbix_filename)
        #except (pyodbc.ProgrammingError):
            #print ('SQL has truncated ' + reportFolder)


def process_file(file_name): # pass in folder name and report name as well
    with open(file1, 'r') as s:
        for line in s:
            process_line(line)

def process_line(line):
    global saved_server, saved_database

    server, database = check_database_record(line)
    if server:
        saved_server = server
        saved_database = database
    view = check_view_record(line)
    if view:
        print(reportFolder, reportName, saved_server, saved_database, view)
        save_view_data(reportFolder, reportName, saved_server, saved_database, view)

def save_view_data(reportFolder, reportName, server, database, view):
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO ODR_DependencyMapping (ReportFolder, ReportName, ServerName, DBName, ViewName, CreatedOn) VALUES (?, ?, ?, ?, ?, ?)", (reportFolder, reportName, server, database, view, datetime.now()))
    conn.commit()

def check_database_record(line):
    m1 = re.search(r'Source = Sql\.[^"]+\("([^"]+)",.*"([^"]+)"', line)
    if m1:
        return m1[1], m1[2]
    return None, None

def check_view_record(line):
    m1 = re.search(r'Item="(\w+)', line)
    if m1:
        return m1[1]
    return None


main()
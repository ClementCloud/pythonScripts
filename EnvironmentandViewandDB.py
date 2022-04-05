import re
a=1
# Open the file for reading
with open('Section1.m') as fd:

  for line in fd:
    text = fd.readline()
    #print('1') 
    rx = re.compile(r'(Item=)([\"a-zA-Z_]+)')
    rx1 = re.compile(r'([-\.a-zA-Z_]+)(.com)')
    rx3 = re.compile(r'(MD)([a-zA-Z_]+)')

    view = rx.finditer(text)
    env = rx1.finditer(text)
    db = rx3.finditer(text)
    for match in view:
      print(a)
      a+= 1
      print(match)
      
    for match in env:
      print(match)
      

    for match in db:
      print(match)  
     




















"""import os
import zipfile
from zipfile import ZipFile
from shutil import copyfile
from datetime import date
import shutil
import subprocess


subprocess.call(['7z', 'a', 'DataMashup' +'.7z', 'DataMashup'])



   for line in fd1:
    text = fd1.readline()
    #print('1')
    rx1 = re.compile(r'^(\s*)("[^"]*"|[^;]*)')
    for line in text.splitlines():
        m1 = rx1.search(line)
        if m1:
            print("{}{}".format(m.group(1), m.group(2).strip('"')))
            """
import os
from zipfile import ZipFile



#OPEN FILES
f1 = open('dst.txt', 'w+')
mylines =[]
with open('Section1.m', 'r') as s:
    #ITERATE THROUGH THE TEXT AND PRINT RESULTS IN A NEW FILE
    for line in s:
      mylines.append(line)
    for element in mylines:
      print (element, end='') 
      print (mylines[0].find('Source =')) 
#ftext = s.readline()
 #       wrd1 = 'Source = '
  ###    res1 = ftext.partition(wrd2)[2] 
 #       f1.write(res + res1)
     #   print(res + res1) 
#
s.close()
f1.close()
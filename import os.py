import os
from zipfile import ZipFile



#OPEN FILES
f1 = open('dst.txt', 'w+')
with open('Section1.m', 'r') as s:
    #ITERATE THROUGH THE TEXT AND PRINT RESULTS IN A NEW FILE
    for myline in s:
        ftext = s.readline()
        wrd1 = 'Source = '
        res = ftext.partition(wrd1)[2] 
        wrd2 = 'Item='
        res1 = ftext.partition(wrd2)[2] 
        f1.write(res + res1)
        print(res + res1) 

s.close()
f1.close()
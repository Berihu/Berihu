# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 16:06:23 2014
@author: BAGS
"""
import csv
import os

rawDataPath=r'D:\MScTHESIS\DATA\ANALYSIS_DATA\PhotoExtractNL_RAW'
cleanedDataPath=r'D:\MScTHESIS\DATA\ANALYSIS_DATA\PhotoExtractNL_CLEANED'


def ReadRawCSV(path):
    os.chdir(path)
    output = []
    dataFile = open( 'NLMeadow.csv','r') #open the file in read universal mod
    csvreader=csv.reader(dataFile,delimiter=',',quotechar='|')
    for row in csvreader:
        output.append(row)
    dataFile.close()
    return output
def CleanPhotoData(lst,path):
    os.chdir(path)
    with open('NLMeadow.csv', 'wb') as envFile:
        envWriter = csv.writer(envFile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        envWriter.writerow(lst[0])
        l1=lst[1:]
        l2=lst[2:]
        for i in range(len(l2)):
            for j in range(len(l2)):
             if ((l1[i][1]==l2[j][1] and l1[i][2]==l2[j][2] and l1[i][3]==l2[j][3] and l1[i][4]==l2[j][4] )== False):
              envWriter.writerow(l1[i])
        envFile.close()

# do the data cleaning
CleanPhotoData(ReadRAWCSV(rawDataPath),cleanedDataPath) 

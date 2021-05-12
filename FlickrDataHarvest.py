# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 05:26:00 2014
@author: B.A.Gidey
"""
import requests
import json
import os
import unicodedata

os.chdir('D:\MScTHESIS\DATA\RAW_PHOTOS')
uriQuery='https://api.flickr.com/services/rest/?method=flickr.photos.search&...' 
'''
 The Uri query should contain all parameters
 Obtain the number of pages of the data returned by the http request for the search term
'''   
def getNumberOfPages():
    r = requests.get(uriQuery)
    commit_data=r.text
    data=json.loads(commit_data)
    return data['photos']['pages']  
'''
   Extract photo information from all available pages for the search term
   and write the resulting data in to a csv file on the local hard disk
'''    
def getPhotoExtract(numberOfPage):
    csvFile=open('eggs.csv','a')
    for page in range( numberOfPage) :
        searcurl=uriQuery+'&page='+str(page+1)
        r = requests.get(searcurl)
        commit_data=r.text
        data=json.loads(commit_data)       
        for  i in range(len(data['photos']['photo'])):
            pid=data['photos']['photo'][i]['id']
            powner=data['photos']['photo'][i]['owner']
            ptitle=data['photos']['photo'][i]['title']
            ptitle=unicodedata.normalize('NFKD', ptitle).encode('ascii','ignore')
            dateTaken=data['photos']['photo'][i]['datetaken']
            tags=data['photos']['photo'][i]['tags']
            tags=unicodedata.normalize('NFKD', tags).encode('ascii','ignore')
            lat=data['photos']['photo'][i]['latitude']
            lon=data['photos']['photo'][i]['longitude']                     
            accuracy=data['photos']['photo'][i]['accuracy']
            str1=str(pid)+','+str(powner)+','+str(ptitle)+','+str(dateTaken)
            str2=str(tags)+','+str(lon)+','+str(lat)+','+str(accuracy)
            strinput=str1+str2
            csvFile.write('\n'+ strinput)
    csvFile.close()   
    
getPhotoExtract(getNumberOfPages())

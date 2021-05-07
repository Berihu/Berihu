# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 15:55:00 2014

@author: BAGS
"""

import pandas as pd
import os 
from scipy.stats import spearmanr
import numpy as np
import datetime
pd.options.display.mpl_style = 'default'

    
'''
 The function generates summary report for both photos and tick bites per land cover
'''   
def GenerateSummaryReport():
     '''
     read photo data
     '''
     os.chdir('D:\MScTHESIS\DATA\ANALYSIS_RESULST\RELATIONSHIPS\PHOTOS_LANDCOVER')
     tempPhoto_df=pd.read_csv('NLPELC10Interset.csv')   
     photos_df= pd.DataFrame(tempPhoto_df)
     photos_data= zip( photos_df['COVETYPE'],photos_df['photoCnt'])
     newPhoto_df=pd.DataFrame(photos_data, columns=['Land_Cover','NumberOfPhotos'])
     photosDataFrame=pd.DataFrame(newPhoto_df.groupby('Land_Cover')['NumberOfPhotos'].sum())
     photos=photosDataFrame.sort('NumberOfPhotos',ascending=True)
     '''
     read tick bite data
     '''
     os.chdir('D:\MScTHESIS\DATA\ANALYSIS_RESULST\RELATIONSHIPS\TICKBITE-LANDCOVER')
     tempTickBite_df=pd.read_csv('NLTOLC10Interset.csv')   
     tickBites_df= pd.DataFrame(tempTickBite_df)
     tickBites_data= zip( tickBites_df['COVETYPE'],tickBites_df['tickCnt'])
     newTickBites_df=pd.DataFrame(tickBites_data, columns=['Land_Cover','NumberOfTickBites'])
     tickBitesDataFrame=pd.DataFrame(newTickBites_df.groupby('Land_Cover')['NumberOfTickBites'].sum())
     tickBites=tickBitesDataFrame.sort('NumberOfTickBites',ascending=True)
     '''
      print data summary
     '''
     print (photos['NumberOfPhotos'],photos['NumberOfPhotos']/photos['NumberOfPhotos'].sum() *100)
     print (tickBites['NumberOfTickBites'],tickBites['NumberOfTickBites']/tickBites['NumberOfTickBites'].sum() *100)
     
     '''
     plot summary reports
     '''
     photos.plot(kind='bar',figsize =(10,5),title='Photos per land cover summary')
     tickBites.plot(kind='barh',figsize =(10,5),title='Tick bites per land cover summary')
 
'''

 The function calculates spearmans correlation for both datasets aggregated by land cover classes
'''  
def EvaluateCorrelationByLandcover():
     os.chdir('D:\MScTHESIS\DATA\ANALYSIS_RESULST\RELATIONSHIPS\TICKBITES_PHOTOS\NEWDATA')
     temp_df=pd.read_csv('NLTOPELANDCOVER10FINAL.csv') 
     temp_dfNZ=pd.read_csv('NLTOPELANDCOVER10FINALNZ.csv')   
     summ_df= pd.DataFrame(temp_df)
     corr_df=pd.DataFrame(temp_dfNZ)
     corr_data= zip( corr_df['FID'],corr_df['Sum_photoC'],corr_df['Sum_tickCn'])
     summ_data= zip( summ_df['COVETYPE'],summ_df['Sum_photoC'],summ_df['Sum_tickCn'])
     corrDataframe=pd.DataFrame(corr_data, columns=['FeatureID','NumberOfPhotos','NumberOfTickBites'])
     newDataframe=pd.DataFrame(summ_data, columns=['Land_Cover','NumberOfPhotos','NumberOfTickBites'])
     df1=pd.DataFrame(newDataframe.groupby('Land_Cover')['NumberOfPhotos','NumberOfTickBites'].sum())
     print   newDataframe.describe()
     print   df1.describe()
     print 'Relationship by land cover Spearmansr:',spearmanr(corrDataframe['NumberOfTickBites'],corrDataframe['NumberOfPhotos'])
   
     df1.plot(kind='barh',figsize =(10,5),title='Tick bites and photos summary')
  
     
     corrDataframe.plot(kind='Scatter', color='purple',xlim=(-10,100),ylim=(-10,300), x='NumberOfTickBites',y='NumberOfPhotos', figsize =(10,5),title=' Tick bite VS Photos per land cover')

'''

 The function calculates spearmans correlation for both datasets aggregated by Municipality
''' 
def EvaluateCorrelationByMuni():
     os.chdir('D:\MScTHESIS\DATA\ANALYSIS_RESULST\RELATIONSHIPS\TICKBITES_PHOTOS\CSV')
     temp_df=pd.read_csv('NLMunicipalitiesFinalAggregate.csv',index_col='FID')   
     photos_df= pd.DataFrame(temp_df)
     corr_data= zip(photos_df['Sum_photoC'],photos_df['Sum_tickCn'])     
     corrDataframe=pd.DataFrame(corr_data, columns=['NumberOfPhotos','NumberOfTickBites'])     
     print 'Relationship byMunicipality Spearmansr:',spearmanr(corrDataframe['NumberOfTickBites'],corrDataframe['NumberOfPhotos'])
     corrDataframe.hist(bins=100, figsize =(15,5))
     
     corrDataframe.plot(kind='scatter',color='purple',xlim=(-10,200),ylim=(-10,700),x='NumberOfTickBites',y='NumberOfPhotos',figsize =(10,5), title=' Tick bite VS Photos per Municipality')
'''
 The function calculates spearmans correlation for both datasets aggregated by Municipality
''' 
def EvaluateTemporalCorrelation():
    os.chdir('D:\MScTHESIS\DATA\ANALYSIS_RESULST\RELATIONSHIPS\TICKBITES_PHOTOS\CSV')
    temp_df=pd.read_csv('NLTO_3YBuiltUP.csv',parse_dates=['datereported'],index_col='datereported')
    mydata=temp_df.resample('1W',how={'ticksCnt': np.sum})
    #os.chdir('D:\MScTHESIS\DATA\ANALYSIS_DATA\PhotoExtractNL_CLEANED')
    tempphoto_df=pd.read_csv('NLPE_3YBuiltUP.csv',parse_dates=['datetaken'],index_col='datetaken')
    myphotodata=tempphoto_df.resample('1W',how={'photosCnt': np.sum})
   
    smallerdata=min(len(mydata),len(myphotodata))-1

    ticksData=mydata['ticksCnt'][:]
    
    photodata=myphotodata['photosCnt'][:]   
    time_df= pd.DataFrame(zip(pd.date_range('1/1/2011', '10/1/2014',freq='1W'),ticksData,photodata), columns=['Weeks','Tick_Observation','Photo_Extracts'])
    time_df.plot(kind='scatter',xlim=(-10,200),ylim=(-10,200),x='Tick_Observation',y='Photo_Extracts',figsize =(8,5), color='purple',title='Tick bites  vs photos ')
    time_df.plot(figsize =(8,5), x=time_df['Weeks'], title='Temporal distribution of tick bites and photos')
  
    print 'Spearmansr:',spearmanr(mydata['ticksCnt'][:smallerdata],myphotodata['photosCnt'][:smallerdata])
      
'''
call the functions
'''

PhotoCorrelationByMuni()
TickBitesCorrelationByMuni()
HighLevelThematicTest()
GenerateSummaryReport()

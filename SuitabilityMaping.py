#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BAGS
#
# Created:     10/03/2014
# Copyright:   (c) BAGS 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import linecache
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

import easygui
import os

#============================
#open the input digital elevetion model
#================================
def opendem():
    demfile=easygui.fileopenbox(msg='You are required to give user inputs', title='GFM2.2014', default=None)
    return demfile

#==================================================
# get the elevation range to calculate the suitable elevation
#

def getElevationRange():
    elevationRange=easygui.multenterbox(msg='Fill in values for the fields.', title='Elevation Range ', fields=('Minimum','Maximum'), values=())
    return elevationRange
#
#get the slope range for calculating the suitable slope
#
def getSlopeRange():
    slopeRange=easygui.multenterbox(msg='Fill in values for the fields.', title='slope Range ', fields=('Minimum','Maximum'), values=())
    return slopeRange
#
#get the aspect range for calculating the suitable aspect
#
def getAspectRange():
    aspectRange=easygui.multenterbox(msg='Fill in values for the fields.', title='Aspect Range ', fields=('Minimum','Maximum'), values=())
    return aspectRange
#========================================================
#
#get the distance from road
#
def getDistaceFromRoad():
    distaceFromRoad=easygui.integerbox(msg='Enter distance', title='Distance From Road ', default='', lowerbound=0, upperbound=5000, image=None, root=None)
    return distaceFromRoad
#
#extract elevation data
#
def readDEMFile(demfile):
    dem1 = np.loadtxt(demfile,skiprows=6)
    return dem1

# display the digital elevation model
def displayDEM(dem):
    plt.imshow(dem)
    plt.show()
#extract suitable elevation based on user inputs
def extractElevation(dem,minElevation,maxElevation):
    maxel=int(maxElevation)
    minel=int(minElevation)
    suitableEl=dem
    for i in range(dem.shape[0]):
        for j in range(dem.shape[1]):
            if dem[i][j] > minel and dem[i][j] < maxel:
                suitableEl[i][j]=1
            else:
                 suitableEl[i][j]=0
    return suitableEl

#
#e Calculate the slope of a DEM
#
def generateSlope(dem):
    '''
    Calculate the slope and gradient of a DEM
    '''
    dem4=dem
    f1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    f2 = f1.transpose()
    g1 = signal.convolve(dem4,f1,mode='valid')
    g2 = signal.convolve(dem4,f2,mode='valid')
    slope = np.sqrt(g1**2 + g2**2)
    return slope
#
#Extract slope based on the user inputs
#
def extractSlope(dem,minSlope,maxSlope):
    '''
    Calculate the slope and gradient of a DEM
    '''
    suitableSlope=dem
    minSlop=int(minSlope)
    maxSlop=int(maxSlope)
    suitableSlope=dem
    for i in range(dem.shape[0]):
        for j in range(dem.shape[1]):
            if dem[i][j]>minSlop and dem[i][j]<maxSlop:
               suitableSlope[i][j]=1
            else:
                 suitableSlope[i][j]=0
    return suitableSlope
##
#
#extract aspect data
#

def generateAspect(dem):
    '''
    Calculate the aspect of a DEM
    '''
    dem4=dem
    f1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    f2 = f1.transpose()
    g1 = signal.convolve(dem4,f1,mode='valid')
    g2 = signal.convolve(dem4,f2,mode='valid')
    aspect = np.arctan2(g2,g1)
    return  aspect
#
#extract aspect based on user imput
#

def extractAspect(dem,minAspect,maxAspect):
    '''

    '''
    suitableAspect=dem
    minAsp=int(minAspect)
    maxAsp=int(maxAspect)
    suitableSlope=dem
    for i in range(dem.shape[0]):
        for j in range(dem.shape[1]):
            if dem[i][j]>minAsp and dem[i][j]<maxAsp:
               suitableAspect[i][j]=1
            else:
                 suitableAspect[i][j]=0

    return  suitableAspect
#
#get the road data
#
def openroad():
    roadshapefile=easygui.fileopenbox(msg='You are required to give user inputs', title='GFM2.2014', default=None)
    return roadshapefile

#=====================================
# get the elevation range to calculate the suitable elevation
#

def getElevationRange():
    elevationRange=easygui.multenterbox(msg='Fill in values for the fields.', title='Elevation Range ', fields=('Minimum','Maximum'), values=())
    return elevationRange
#
#get the slope range for calculating the suitable slope
#
def getSlopeRange():
    slopeRange=easygui.multenterbox(msg='Fill in values for the fields.', title='slope Range ', fields=('Minimum','Maximum'), values=())
    return slopeRange
#
#get the aspect range for calculating the suitable aspect
#
def getAspectRange():
    aspectRange=easygui.multenterbox(msg='Fill in values for the fields.', title='Aspect Range ', fields=('Minimum','Maximum'), values=())
    return aspectRange

#
#get the distance from road
#
def getDistaceFromRoad():
    distaceFromRoad=easygui.integerbox(msg='Enter distance', title='Distance From Road ', default='', lowerbound=0, upperbound=5000, image=None, root=None)
    return distaceFromRoad

##extractSlope(extractElevation)
demfile=readDEMFile(opendem())

##displayDEM(demfile)
##
plt.imshow(generateSlope(demfile))
plt.show()
##
plt.imshow(generateAspect(demfile))
plt.show()

##aspect=generateAspect(demfile)
##slope=generateSlope(demfile)
####for i in range(50):
####    print aspect[i][i],"  ",slope[i][i]
##
##print aspect.shape, "    ", slope.shape ,"  ", demfile.shape


##print "aspect ", getAspectRange()
##print "slope ",getSlopeRange()
##print "elevation", getElevationRange()

elevation=getElevationRange()
aspect=getAspectRange()
slope=getSlopeRange()
extractedel=extractElevation(demfile,elevation[0],elevation[1])
extractedslop=extractSlope(generateSlope(demfile),slope[0],slope[1])
extractedaspect=extractAspect(generateAspect(demfile),aspect[0],aspect[1])



print ("extracted elevation\n",extractedel.shape)
print ("extracted slope\n",extractedslop.shape)
print ("extracted aspect\n",extractedaspect.shape)






# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 18:30:31 2017

@author: Paulia
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

source=pd.read_csv(r'D:\marscraters.csv',low_memory=False)

rows=len(source['DIAM_CIRCLE_IMAGE'].index)
print rows

sub1=source[source['DIAM_CIRCLE_IMAGE']>10]
len_sub1=len(sub1.index)
print len_sub1

print str(len_sub1*100/rows)+'%'

#creating craters' map
sub2=source[source['DIAM_CIRCLE_IMAGE']>10]
y=sub2['LATITUDE_CIRCLE_IMAGE'].tolist()
x=sub2['LONGITUDE_CIRCLE_IMAGE'].tolist()
plt.scatter(x,y,s=1)
plt.plot([-180, 180], [0, 0], color='k', linestyle='-', linewidth=2)
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.xlabel('latitude of craters')
plt.ylabel('longitude of craters')
plt.title('Map Of Craters On Mars')
plt.xticks(np.arange(-180, 181, 30))
plt.yticks(np.arange(-90, 91, 10))

#creating histogram of craters' diameters
plt.figure()
plt.hist(source['DIAM_CIRCLE_IMAGE'],bins=np.arange(1,10,0.25),
          edgecolor = "black", zorder=3)
plt.grid(True,linestyle='--',fillstyle='bottom',zorder=0)
plt.xlabel('diameter of craters [km]')
plt.ylabel('number of craters')
plt.title("distribution of craters' diameter")
plt.xlim(1,10)
print 'mean diameter:',round(source['DIAM_CIRCLE_IMAGE'].mean(),2),'[km]'
print 'diameter standard deviation:',round(source['DIAM_CIRCLE_IMAGE'].std(),2),'[km]'

#creating histogram of craters' longitude
plt.figure()
plt.hist(source['LONGITUDE_CIRCLE_IMAGE'],bins=np.arange(-180,181,20),
         edgecolor = "black", zorder=3)
plt.grid(True,linestyle='--',fillstyle='bottom',zorder=0)
plt.xlabel('longitude of craters [deg]')
plt.title("count of craters' longitude")
plt.xlim(-180,180)
plt.xticks(np.arange(-180, 181, 20))

print 'mean longitude:',round(source['LONGITUDE_CIRCLE_IMAGE'].mean(),2),'[deg]'
print 'longitude standard deviation:',round(source['LONGITUDE_CIRCLE_IMAGE'].std(),2),'[deg]'

#creating histogram of craters' latitude
plt.figure()
plt.hist(source['LATITUDE_CIRCLE_IMAGE'],bins=np.arange(-90,91,10),
         edgecolor = "black", zorder=3)
plt.grid(True,linestyle='--',fillstyle='bottom',zorder=0)
plt.xlabel('latitude of craters [deg]')
plt.title("count of craters' latitude")
plt.xticks(np.arange(-90, 91, 10))
plt.yticks(np.arange(0, 50001, 5000))

print 'mean latitude:',round(source['LATITUDE_CIRCLE_IMAGE'].mean(),2),'[deg]'
print 'latitude standard deviation:',round(source['LATITUDE_CIRCLE_IMAGE'].std(),2),'[deg]'
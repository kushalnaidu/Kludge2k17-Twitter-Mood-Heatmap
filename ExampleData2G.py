# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:26:23 2017

@author: kusha
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 08:55:35 2017

@author: kusha
"""

import pandas as pd
df=pd.read_csv("data.csv");
pp=df['Pos']
latitudes=df['Lat']
longitudes=df['Longi']
negative=df["Neg"]
negative=negative/3;
print negative
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pylab import rcParams
rcParams['figure.figsize'] = 15,10
from scipy.misc import imread
fig5 = plt.figure()
ax5 = fig5.add_subplot(111, aspect='equal')
count=0

df.to_csv("Dangerdata.csv")
nneg=[]
for i in range(len(negative)):
    nneg.append((negative[i]-min(negative))/((max(negative)-min(negative))*1.0))
#print nneg

#print len(nneg)
#print len(latitudes)
for i in range(49):
        
        #print i+5,j+6465
        
        if(negative[i]<20):
            
            p=patches.Circle((((latitudes[i]+2.5)*46.67),(longitudes[i]+2.5)*46.67), 2.5*140/3.0,alpha=(30-negative[i])/80.0)
            p.set_facecolor('g')
        else:
          
            p=patches.Circle((((latitudes[i]+2.5)*46.67),(longitudes[i]+2.5)*46.67), 2.5*140/3.0,alpha=negative[i]/85.0)
            p.set_facecolor('r')  
        ax5.add_patch(p)
if(max(negative)>=80):
    SerialOut.output()
#p=patches.Circle((0,0), 5*50/3,alpha=0.1)
#ax5.add_patch(p)
#fig5.savefig('circle5.png', dpi=90, bbox_inches='tight')
ax5.set_ylabel('Longitude')
ax5.set_xlabel('Latitude')

import numpy as np
ax5.set_yticks(np.arange(7),[12.85,12.90,12.95,13,13.05,13.1,13.15])
ax5.set_xticks(np.arange(7),[77.45,77.5,77.55,77.6,77.65,77.70,77.75])
img=imread("./pic.jpg")
plt.imshow(img,extent=[0, 1400, 0, 1400])
fig5.savefig('circles.png', dpi=90, bbox_inches='tight')
#img=Image.open('circle5.png')
#img.show()
#plt.show()
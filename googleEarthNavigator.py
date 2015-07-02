'''
Created on 2014-2-18

@author: yutings
'''

import win32com.client

earth = win32com.client.Dispatch("GoogleEarth.ApplicationGE")

#print earth.isInitialized()

latitude               =41.487942
longitude            =-81.6865                   # Longitude in degrees. Between -180 and 180.
altitude               =100                           # in meters
tilt                      =0                             # looking to the horizon=90, looking to the center of Earth=0
azimuth              =370                          # looking North=0, East=90, South=180, West=270
speed                =0.3                           # speed transition. must be >= 0, above 5.0 the transition is instantaneous
altMode             =1                             #Altitude mode that defines altitude reference origin (1=above ground, 2=absolute)
focusDistance     =100

earth.SetCameraParams (latitude, longitude, altitude, altMode, focusDistance, tilt, azimuth, speed)


#earth.openKmlfile("C:\Users\yutings\Desktop\Map1.kml",True)

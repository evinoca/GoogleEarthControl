# -*- coding: cp936 -*-
'''
Created on 2014-2-20
@author: Audric

Here i want to build a basic toy which is to detect all the fish in a pool or a lake.
Try not to fail a friend's wish.

'''




class boat():
    def __init__():
        print "Hi, I am a boat"

    def __del__():
        print "Bye, i will be gone"

    def move(locationAxis_Array):
        '''
        core action
        '''
        print "Moving to :"+locationAxis_Array[0]+locationAxis_Array[1]

    def steering(angle_degree_Double):
        if angle_degree_Double<0:
            print "Turning left for "+str(abs(angle_degree_Double))+"Degree"
        else:
            print "Turning right for "+str(abs(angle_degree_Double))+"Degree"

    def changePowerOutput():
        pass

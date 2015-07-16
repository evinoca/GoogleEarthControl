#encoding: utf-8



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

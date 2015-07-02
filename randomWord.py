'''
Created on 2014-2-20

@author: yutings
'''
import random

stringList = []

if __name__ == '__main__':
    print "Start"
    while(True):
        string = raw_input()
        if string == ""  and len(stringList)>4:
            i = 0
            output = []
            while i<3:
                word = random.choice(stringList)
                if word not in output:
                    output.append(word)
                    i+=1
                                    
            print output
        else:
            stringList.append(string)
            print "Add: ",string
            
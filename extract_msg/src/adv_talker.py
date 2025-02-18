#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
import serial  
import time

arduino = serial.Serial('/dev/ttyACM1', 9600, timeout=.1)


def callback(data):
    valL=data.x
    if (valL == 0.0):
    	valL=str("000")
    else:    
	valL=str(int(valL))
    
    valR=data.y
    if (valR == 0.0):
    	valR=str("000")
    else:  
        valR=str(int(valR))
    
    valD=data.z
    if (valD == 0.0):
    	valD=str("0")
    else:  
	valD=str(int(valD))
    
    val= valL + " " + valR + " " + valD + " " + '\0'
    
    rospy.loginfo(val)
    arduino.write(val)
    
def listener():

    rospy.init_node('pwmreciver', anonymous=True)

    rospy.Subscriber("rover_drive", Point , callback)

    rospy.spin()

if __name__ == '__main__':
    listener()



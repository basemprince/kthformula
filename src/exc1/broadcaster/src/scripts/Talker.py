#!/usr/bin/env python

import random
import sys
import rospy
from std_msgs.msg import UInt16


def talker():
    pub = rospy.Publisher('Shaker', UInt16, queue_size=10)
    rospy.init_node('talker')
    rate = rospy.Rate(20)
    k = random.randint(1, 2 ** 16)
    n = 4
    while not rospy.is_shutdown(): 
        if (k >= 2 ** 16):
            k = random.randint(1, 2 ** 16)  
        else:
            info = "generating a k = %s" % k
            rospy.loginfo(info) 
            pub.publish(k)
            k += n

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
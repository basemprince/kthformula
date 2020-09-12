#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16 , UInt32

def callback(data):
    q = 0.15
    pub = rospy.Publisher('result', UInt32, queue_size=10)
    x = UInt32 (int (data.data/q))
    rospy.loginfo("recevied k is %s, publishing x to result as %s", data.data, x)
    pub.publish(x)
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener')#, anonymous=True)

    rospy.Subscriber("Shaker", UInt16, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    listener()
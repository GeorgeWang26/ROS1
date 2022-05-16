#! /usr/bin/python3
import rospy
from std_msgs.msg import String

if __name__=='__main__':
    rospy.init_node('publisher_node')
    pub = rospy.Publisher("my_topic", String, queue_size=10)
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        msg=String()
        msg.data = str(["Any messagve you want", 999, True])
        pub.publish(msg)
        rate.sleep()
    rospy.loginfo("Node was stopped")


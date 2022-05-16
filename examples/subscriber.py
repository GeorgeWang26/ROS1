#! /usr/bin/python3
import rospy
from std_msgs.msg import String

def callback_receive_data(msg):
    rospy.loginfo("Message received: ")
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node('subscriber_node')
    sub = rospy.Subscriber("/my_topic", String, callback_receive_data)

    rospy.spin() #keep the script waiting for the callback


#! /usr/bin/python3
import rospy
if __name__=='__main__':
    rospy.init_node("my_python_node") #initializing the node. The name must be unique.
    rospy.loginfo("This node has been started")
    rospy.sleep(1)
    rate=rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
        rospy.loginfo("Hello   " + str(count))
        rate.sleep()
        count += 1

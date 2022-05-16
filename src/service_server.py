#! /usr/bin/python3
import rospy
from rospy_tutorials.srv import AddTwoInts

def handle_add_together(req):
    result = req.a + req.b
    rospy.loginfo("summation of " + str(req.a) + " and " + str(req.b) + " is " + str(result))
    return result

if __name__ == '__main__':
    rospy.init_node("sum_server")
    rospy.loginfo("summation")
    service = rospy.Service("/add_two_ints", AddTwoInts, handle_add_together)
    rospy.loginfo("Service server has been started")

    rospy.spin()


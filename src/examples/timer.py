import rospy

def my_callback(event):
    print('Timer called at ' + str(event.current_real))
if __name__ == "__main__":
    rospy.init_node("timer")
    rospy.Timer(rospy.Duration(2), my_callback)

    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        print("from loop")
        r.sleep()
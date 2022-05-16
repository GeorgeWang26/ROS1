import os
# os.environ["ROS_NAMESPACE"] = "/ros_space"
print(os.environ["ROS_ROOT"])
# print(os.environ["ROS_NAMESPACE"])

import rospy

if __name__ == '__main__':
    rospy.init_node("parameter_server_1");
    rospy.set_param("/abs_path", 1)
    rospy.set_param("under_namespace/msg", "hello there")
    rospy.set_param("~private_path", True)

    print(rospy.get_param_names())
    print(rospy.has_param("/abs_path"), rospy.has_param("abs_path"), rospy.has_param("~abs_path"))
    print(rospy.has_param("/under_namespace"), rospy.has_param("under_namespace"), rospy.has_param("~under_namespace"))
    print(rospy.has_param("/private_path"), rospy.has_param("private_path"), rospy.has_param("~private_path"))

    print(rospy.get_param("/")["abs_path"])
    print(rospy.get_param("/under_namespace")["msg"])
    print(rospy.get_param("/parameter_server_1/private_path"))
    

    print(rospy.get_name())
    print(rospy.get_namespace())
    print(rospy.get_node_uri())
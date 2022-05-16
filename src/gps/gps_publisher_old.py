import rospy
from std_msgs.msg import String
import pynmea2
import serial

data = {"latitude": 0, "logitude": 0}

def pub_msg(event):
    pub.publish(str(data))
    print(data)


if __name__ == "__main__":
    rospy.init_node("gps_publisher")
    pub = rospy.Publisher("/gps/fix", String, queue_size = 1)
    # rate = rospy.Rate(1)
    gps = serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = 0.5)
    rospy.Timer(rospy.Duration(1), pub_msg, oneshot=False)
    
    while True:
        s = gps.readline().decode("utf-8")
        # print(s)
        if s[0:6] == "$GPGGA":
            msg = pynmea2.parse(s)
            data = {"latitude": msg.latitude, "logitude": msg.longitude}

        if rospy.is_shutdown():
            break

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

def tof_callback(data):
    if data.range < 0.8:  # Stop 80cm away from an object
        stop()
    else:
        move_forward()

def stop():
    cmd = Twist()
    cmd.linear.x = 0
    cmd.angular.z = 0
    pub.publish(cmd)

def move_forward():
    cmd = Twist()
    cmd.linear.x = 0.1  # Move forward slowly
    cmd.angular.z = 0
    pub.publish(cmd)

def navigation_node():
    rospy.init_node('navigation_node')
    global pub
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('tof_data', Range, tof_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        navigation_node()
    except rospy.ROSInterruptException:
        pass


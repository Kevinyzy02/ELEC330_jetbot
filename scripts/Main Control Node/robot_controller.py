#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def duck_callback(data):
    rospy.loginfo(data.data)
    if "detected" in data.data:
        _, x, _ = data.data.split()
        adjust_movement(int(x))
    else:
        stop()

def stop():
    cmd = Twist()
    cmd.linear.x = 0
    cmd.angular.z = 0
    pub.publish(cmd)

def adjust_movement(x):
    cmd = Twist()
    if x < 320 - 50:  # Adjust left if duck is to the left of center
        cmd.angular.z = 0.1
    elif x > 320 + 50:  # Adjust right if duck is to the right of center
        cmd.angular.z = -0.1
    else:  # Stop turning when approximately centered
        cmd.angular.z = 0
        cmd.linear.x = 0.05  # Slowly move forward
    pub.publish(cmd)

def robot_controller():
    rospy.init_node('robot_controller')
    global pub
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('duck_position', String, duck_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        robot_controller()
    except rospy.ROSInterruptException:
        pass

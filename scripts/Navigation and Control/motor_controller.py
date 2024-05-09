#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from your_motor_driver import MotorDriver  # Adjust import as necessary

def command_callback(cmd):
    motor.set_speed(cmd.linear.x)
    motor.set_turn(cmd.angular.z)

def motor_controller():
    rospy.init_node('motor_controller')
    global motor
    motor = MotorDriver()  # Initialize motor
    rospy.Subscriber('cmd_vel', Twist, command_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        motor_controller()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Range
from vl53l5cx import VL53L5CX

def tof_publisher():
    rospy.init_node('tof_publisher')
    pub = rospy.Publisher('tof_data', Range, queue_size=10)
    tof = VL53L5CX()
    range_msg = Range()
    range_msg.radiation_type = Range.INFRARED
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        range_msg.range = tof.get_distance()
        pub.publish(range_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        tof_publisher()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from I2CEncoderMini import I2CEncoderMini

def encoder_publisher():
    rospy.init_node('encoder_publisher')
    pub = rospy.Publisher('encoder_data', Int32, queue_size=10)
    encoder = I2CEncoderMini(address=0x40)  # Specify the correct I2C address
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        count = encoder.read_counter()
        pub.publish(count)
        rate.sleep()

if __name__ == '__main__':
    try:
        encoder_publisher()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from lsm303d import LSM303D

def imu_publisher():
    rospy.init_node('imu_publisher')
    pub = rospy.Publisher('imu_data', Imu, queue_size=10)
    imu = LSM303D()
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        accel, mag = imu.get_accel(), imu.get_mag()
        imu_msg = Imu()
        imu_msg.linear_acceleration.x = accel.x
        imu_msg.linear_acceleration.y = accel.y
        imu_msg.linear_acceleration.z = accel.z
        imu_msg.angular_velocity.x = mag.x  # Assuming conversion factor or calibration
        imu_msg.angular_velocity.y = mag.y
        imu_msg.angular_velocity.z = mag.z
        pub.publish(imu_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass


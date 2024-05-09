#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import numpy as np

def detect_yellow_object(image_message):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image_message, desired_encoding='bgr8')
    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Threshold for duck size
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(cv_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            pub.publish("detected {} {}".format(x+w//2, y+h//2))
            break
    cv2.imshow('Duck Detection', cv_image)
    cv2.waitKey(3)

def object_detector():
    rospy.init_node('object_detector')
    global pub
    pub = rospy.Publisher('duck_position', String, queue_size=10)
    rospy.Subscriber("camera_image", Image, detect_yellow_object)
    rospy.spin()

if __name__ == '__main__':
    try:
        object_detector()
    except rospy.ROSInterruptException:
        pass


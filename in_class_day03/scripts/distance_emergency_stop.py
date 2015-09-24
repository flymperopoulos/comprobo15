#!/usr/bin/env python
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

import time

c = False
rospy.init_node('laser_distance_node')

def stop_callback(velocity):
	velocity.linear.x = 0

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "%s", data.ranges[0])
	lin_vel_y = Twist(linear=Vector3(x=1))

	if (data.ranges[0]<=1.0) and (data.ranges[0]>=0.50):
		stop_callback(lin_vel_y)
		c = True


	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	pub.publish(lin_vel_y)


def run():
    bump_listener = rospy.Subscriber("/scan", LaserScan, callback, queue_size=1)
    rospy.spin()

while not rospy.is_shutdown():
	if c==False:
		run()
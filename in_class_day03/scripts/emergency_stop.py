#!/usr/bin/env python
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3
from neato_node.msg import Bump

import time


rospy.init_node('bump_node')

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "%s", data)
	lin_vel_y = Twist(linear=Vector3(x=1))

	if (data.leftFront) or (data.rightFront):
		lin_vel_y.linear.x = 0

	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	pub.publish(lin_vel_y)


def run():
    bump_listener = rospy.Subscriber("/bump", Bump, callback, queue_size=1)
    rospy.spin()

while not rospy.is_shutdown():
	run()
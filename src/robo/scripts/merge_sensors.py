#!/usr/bin/env python3

import rospy
from robo.msg import MergedReadings
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import message_filters


def callback(laser: LaserScan, odometry: Odometry):
    rospy.loginfo("hello from  the callback")
    msg = MergedReadings()
    msg.header = laser.header
    msg.laser = laser
    msg.odometry = odometry
    pub.publish(msg)


if __name__ == '__main__':
    try:
        rospy.init_node("node_merge_sensor_readings")
        rospy.loginfo("node_merge_sensor_readings is up and running")
        # front_laser readings and rear_laser readings are merged using laser_scan_multi_merger, and the output is redirected to a link named "/scan_multi"
        laser_sub = message_filters.Subscriber("/scan_multi", LaserScan)

        odometry_sub = message_filters.Subscriber(
            "/robot/robotnik_base_control/odom", Odometry)

        pub = rospy.Publisher("all_readings", MergedReadings, queue_size=1)

        time_synchronizer = message_filters.ApproximateTimeSynchronizer(
            [laser_sub, odometry_sub], queue_size=1, slop=0.01)
        time_synchronizer.registerCallback(callback)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
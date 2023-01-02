#!/usr/bin/env python3

import rospy
from robo.msg import LocalizationReadings
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
import message_filters


def callback(laser: LaserScan, pose: PoseStamped):
    print("Publishing Localized readings")
    msg = LocalizationReadings()
    msg.header = laser.header
    msg.laser = laser
    msg.pose = pose
    pub.publish(msg)


if __name__ == '__main__':
    try:
        rospy.init_node("node_ekf_on_sensors")
        rospy.loginfo("node_ekf_on_sensors is up and running")
        # front_laser readings and rear_laser readings are merged using laser_scan_multi_merger, and the output is redirected to a link named "/scan_multi"
        laser_sub = message_filters.Subscriber("/scan_multi", LaserScan)

        pose_sub = message_filters.Subscriber(
            "/ekf_model", PoseStamped)

        pub = rospy.Publisher("correct_readings", LocalizationReadings, queue_size=10)

        time_synchronizer = message_filters.ApproximateTimeSynchronizer(
            [laser_sub, pose_sub], queue_size=1, slop=0.01)
        time_synchronizer.registerCallback(callback)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
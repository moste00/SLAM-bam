#!/usr/bin/env python3

import rospy
from robo.msg import MergedReadings
from nav_msgs.msg import OccupancyGrid, MapMetaData, Odometry
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Quaternion, Pose, Point
from std_msgs.msg import Header
from skimage.draw import line
import tf.transformations as tft
import numpy as np
from enum import Enum

INT = np.int16


class RVIZ():
    RESOLUTION = 0.1
    WIDTH = 1500
    HEIGHT = 1500
    ORIGIN_X = -50
    ORIGIN_Y = -50
    MAX_RANGE = 30
    MIN_RANGE = 0.1
    MAX_ANGLE = np.math.pi
    MIN_ANGLE = -np.math.pi
    FRAME_ID = "robot_map"


class Map:

    def __init__(self):
        self.occupancy_grid = OccupancyGrid(
            Header(frame_id=RVIZ.FRAME_ID),
            MapMetaData(rospy.Time(), RVIZ.RESOLUTION, RVIZ.WIDTH, RVIZ.HEIGHT,
                        Pose()),
            np.ones((RVIZ.HEIGHT, RVIZ.WIDTH), dtype=INT) * -1)

        self.occupancy_grid.info.origin.position.x = RVIZ.ORIGIN_X
        self.occupancy_grid.info.origin.position.y = RVIZ.ORIGIN_Y
        self.hits = np.ones((RVIZ.HEIGHT, RVIZ.WIDTH), dtype=INT)
        self.misses = np.ones((RVIZ.HEIGHT, RVIZ.WIDTH), dtype=INT)

    def xy2ij(self, x, y):
        cc = (x - RVIZ.ORIGIN_X) / RVIZ.RESOLUTION
        rr = (y - RVIZ.ORIGIN_Y) / RVIZ.RESOLUTION
        return np.array(rr, dtype=INT), np.array(cc, dtype=INT)

    def get_pose(self, odom: Odometry):
        x, y, z, w = odom.pose.pose.orientation.x, \
                     odom.pose.pose.orientation.y, \
                     odom.pose.pose.orientation.z, \
                     odom.pose.pose.orientation.w
        _, _, theta = tft.euler_from_quaternion([x, y, z, w])
        px, py = self.xy2ij(odom.pose.pose.position.x,
                            odom.pose.pose.position.y)
        return px, py, theta

    def is_inside(self, x, y):
        return 0 <= x * RVIZ.RESOLUTION < RVIZ.WIDTH and 0 <= y or y * RVIZ.RESOLUTION < RVIZ.HEIGHT

    def build_map(self, merged_readings: MergedReadings):

        laser = merged_readings.laser
        odom = merged_readings.odometry

        dists = np.array(laser.ranges) / RVIZ.RESOLUTION

        true_x, true_y, true_theta = self.get_pose(odom)

        angle_array = np.arange(RVIZ.MIN_ANGLE + true_theta,
                                RVIZ.MAX_ANGLE + true_theta,
                                laser.angle_increment)

        end_x = true_x + dists * np.cos(angle_array)
        end_y = true_y + dists * np.sin(angle_array)

        for i in range(len(dists)):

            if not self.is_inside(true_x, true_y):
                break

            d = dists[i]
            dx = (end_x[i] - true_x) / d
            dy = (end_y[i] - true_y) / d
            xs = np.arange(true_x, end_x[i] - dx, dx).astype(INT)
            ys = np.arange(true_y, end_y[i] - dy, dy).astype(INT)

            min_len = min(len(xs), len(ys))
            xs = xs[:min_len]
            ys = ys[:min_len]

            self.misses[ys, xs] += 1

        self.hits[end_y.astype(INT), end_x.astype(INT)] += 1
        self.occupancy_grid.data = np.round(self.hits /
                                            (self.hits + self.misses) *
                                            100).astype(dtype=INT).flatten()


def map_callback(data):
    my_map.build_map(data)
    pub.publish(my_map.occupancy_grid)
    my_map.hits = np.ones((RVIZ.HEIGHT, RVIZ.WIDTH), dtype=INT)
    my_map.misses = np.ones((RVIZ.HEIGHT, RVIZ.WIDTH), dtype=INT)


if __name__ == '__main__':
    try:
        rospy.init_node("node_map")
        rospy.loginfo("node_map is up and running")
        my_map = Map()
        sensor_sub = rospy.Subscriber("/all_readings", MergedReadings,
                                      map_callback)
        pub = rospy.Publisher("map_topic", OccupancyGrid, queue_size=1)
        while not rospy.is_shutdown():
            rospy.spin()

    except rospy.ROSInterruptException:
        pass
#!/usr/bin/env python3

import rospy
from robo.msg import MergedReadings
import numpy as np
import tf.transformations as tft
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped


class EKF_Model:
    ALPHA_1 = 0.2
    ALPHA_2 = 0.03
    ALPHA_3 = 0.09
    ALPHA_4 = 0.08

    SIGMA_R = 0.08
    SIGMA_PHI = 0.08
    SIGMA_S = 0.05

    def __init__(self):
        self.u = np.array([0, 0, 0])
        self.cov = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.prev_time = rospy.Time.now().to_sec()
        
    def predict(self, twist: Twist):
        print("Predicting:")
        delta_t = rospy.Time.now().to_sec() - self.prev_time
        self.prev_time = rospy.Time.now().to_sec()
        v = twist.linear.x
        w = twist.angular.z

        angle = self.u[2] + w * delta_t / 2
        self.u = self.u + np.array([
            v * delta_t * np.cos(angle), v * delta_t * np.sin(angle),
            w * delta_t
        ])
        angle = self.u[2] + w * delta_t / 2
        G = np.array([[1, 0, -v * delta_t * np.sin(angle)],
                      [0, 1, v * delta_t * np.cos(angle)], [0, 0, 1]])
        V = np.array([[np.cos(angle), -0.5 * np.sin(angle)],
                      [np.sin(angle), 0.5 * np.cos(angle)], [0, 1]])

        M = np.array([[EKF_Model.ALPHA_1 * v**2 + EKF_Model.ALPHA_2 * w**2, 0],
                      [0,
                       EKF_Model.ALPHA_3 * v**2 + EKF_Model.ALPHA_4 * w**2]])
        self.cov = np.dot(np.dot(G, self.cov), G.T) + np.dot(np.dot(V, M), V.T)

    def correct(self, data: MergedReadings):
        print("Correcting")
        odom = data.odometry
        x = odom.pose.pose.position.x
        y = odom.pose.pose.position.y
        orientation = odom.pose.pose.orientation
        orientation = [
            orientation.x, orientation.y, orientation.z, orientation.w
        ]
        _, _, yaw = tft.euler_from_quaternion(orientation)

        Z = np.array([x, y, yaw])

        Q = np.array([[EKF_Model.SIGMA_R, 0, 0], [0, EKF_Model.SIGMA_PHI, 0],
                      [0, 0, EKF_Model.SIGMA_S]])

        C = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        K = self.cov @ C.T @ np.linalg.inv(C @ self.cov @ C.T + Q)
        self.u = self.u + K @ (Z - C @ self.u)
        self.cov = (np.eye(3) - K @ C) @ self.cov

        print(self.u[0],self.u[1])

        self.publish()

    def publish(self):
        print("Publishing")
        roll, pitch, yaw = tft.euler_from_quaternion([0, 0, 0, 1])

        pose_stamped = PoseStamped()
        pose_stamped.pose.position.x = self.u[0]
        pose_stamped.pose.position.y = self.u[1]
        pose_stamped.pose.position.z = 0

        q = tft.quaternion_from_euler(roll, pitch, self.u[2])
        pose_stamped.pose.orientation.x = q[0]
        pose_stamped.pose.orientation.y = q[1]
        pose_stamped.pose.orientation.z = q[2]
        pose_stamped.pose.orientation.w = q[3]
        pose_stamped.header.frame_id = 'robot_map'
        pose_stamped.header.stamp = rospy.Time.now()

        pub.publish(pose_stamped)


if __name__ == "__main__":
    rospy.init_node("node_ekf_model")
    rospy.loginfo("node_ekf_model is up and running")
    ekf_model = EKF_Model()
    pub = rospy.Publisher("/ekf_model", PoseStamped,queue_size=10)

    rospy.Subscriber("/robot/robotnik_base_control/cmd_vel", Twist, ekf_model.predict)
    rospy.Subscriber("/all_readings", MergedReadings, ekf_model.correct)
    rospy.spin()

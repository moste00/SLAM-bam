#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

#Keyboard input 
import sys 
from select import select
PLATFORM = sys.platform
if PLATFORM == 'win32': #Operating System Detection
    import msvcrt #Windows API
else:
    import termios #POSIX API
    import tty

def get_key(timeout : float):
     if PLATFORM == 'win32':
         # getwch() returns a string on Windows
         key = msvcrt.getwch()
     else:
         tty.setraw(sys.stdin.fileno())
         # sys.stdin.read() returns a string on Linux
         rlist, _, _ = select([sys.stdin], [], [], timeout)
         if rlist:
             key = sys.stdin.read(1)
         else:
             key = ''
         termios.tcsetattr(sys.stdin, termios.TCSADRAIN,termios.tcgetattr(sys.stdin))
     return key
 
def brake(velocity):
    if velocity < 0.0:
        velocity += 0.2
        if velocity > 0.0: velocity = 0.0
    elif velocity > 0.0:
        velocity -= 0.2
        if velocity < 0.0: velocity = 0.0
    
    return velocity

if __name__ == "__main__":
    rospy.init_node(f"Keyboard_Controller_Node")
    vel_pub = rospy.Publisher("/robot/robotnik_base_control/cmd_vel",
                              Twist,
                              queue_size= 100) 
    rate = rospy.Rate(60)


    forward = 0.0
    left = 0.0
    while not rospy.is_shutdown():
        key = get_key(timeout= 0.1)
        if key == "A" or key == "a":
            left += 1.0
        elif key == "D" or key == "d":
            left += -1.0
        elif key == "W" or key == "w":
            forward += 1.0
        elif key == "S" or key == "s":
            forward += -1.0
        else:
            forward = brake(forward)
            left = brake(left)

        cmd = Twist()
        cmd.linear.x = forward
        cmd.angular.z = left

        vel_pub.publish(cmd)
        rate.sleep()
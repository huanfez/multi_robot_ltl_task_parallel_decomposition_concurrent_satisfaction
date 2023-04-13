#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, PoseWithCovariance, Vector3
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
import numpy as np
import copy

import actionlib
from mrs_taskplan.msg import TaskAction, TaskGoal, TaskResult, TaskFeedback

from Khepera_server_class2 import KepRobot


# robot 8
try:
    # geometry_name, agent_radius, agent_id, v_max, initial_position
    currentDir = '/home/hz/catkin_ws/src/eight_mrs_taskplan/node/results/'
    textfile8_d = open(currentDir + 'traj8d.txt', 'w')
    textfile8_a = open(currentDir + 'traj8a.txt', 'w')

    kepherarobot8 = KepRobot('ColumbusCirclePoly', 0.177, 7, 0.20, [3.5, 2.5],\
       '/tb3_7/cmd_vel', '/tb3_7/odom', [textfile8_d, textfile8_a], 0.05, [])

    kepherarobot8.task_server.start()

    rospy.spin()
    textfile8_d.close()
    textfile8_a.close()
except rospy.ROSInterruptException:
    pass

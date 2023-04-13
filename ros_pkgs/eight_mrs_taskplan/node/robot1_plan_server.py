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

from Khepera_server_class import KepRobot


# robot 1
try:
    # geometry_name, agent_radius, agent_id, v_max, initial_position
    currentDir = '/home/hz/catkin_ws/src/eight_mrs_taskplan/node/results/'
    textfile1_d = open(currentDir + 'traj1d.txt', 'w')
    textfile1_a = open(currentDir + 'traj1a.txt', 'w')

    kepherarobot1 = KepRobot('ColumbusCirclePoly', 0.177, 0, 0.20, [0.5, 0.5],\
       '/tb3_0/cmd_vel', '/tb3_0/odom', [textfile1_d, textfile1_a], 0.05, [])

    kepherarobot1.task_server.start()

    rospy.spin()
    textfile1_d.close()
    textfile1_a.close()
except rospy.ROSInterruptException:
    pass

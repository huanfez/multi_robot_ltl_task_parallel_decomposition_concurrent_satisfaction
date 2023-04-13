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


# robot 7
try:
    # geometry_name, agent_radius, agent_id, v_max, initial_position
    currentDir = '/home/hz/catkin_ws/src/eight_mrs_taskplan/node/results/'
    textfile7_d = open(currentDir + 'traj7d.txt', 'w')
    textfile7_a = open(currentDir + 'traj7a.txt', 'w')

    kepherarobot7 = KepRobot('ColumbusCirclePoly', 0.177, 6, 0.20, [3.5, 0.5],\
       '/tb3_6/cmd_vel', '/tb3_6/odom', [textfile7_d, textfile7_a], 0.05, [])

    kepherarobot7.task_server.start()

    rospy.spin()
    textfile7_d.close()
    textfile7_a.close()
except rospy.ROSInterruptException:
    pass

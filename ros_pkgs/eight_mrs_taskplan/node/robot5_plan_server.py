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


# robot 5
try:
    # geometry_name, agent_radius, agent_id, v_max, initial_position
    currentDir = '/home/hz/catkin_ws/src/eight_mrs_taskplan/node/results/'
    textfile5_d = open(currentDir + 'traj5d.txt', 'w')
    textfile5_a = open(currentDir + 'traj5a.txt', 'w')

    kepherarobot5 = KepRobot('ColumbusCirclePoly', 0.177, 4, 0.20, [0.5, 0.5],\
       '/tb3_4/cmd_vel', '/tb3_4/odom', [textfile5_d, textfile5_a], 0.05, [])

    kepherarobot5.task_server.start()

    rospy.spin()
    textfile5_d.close()
    textfile5_a.close()
except rospy.ROSInterruptException:
    pass

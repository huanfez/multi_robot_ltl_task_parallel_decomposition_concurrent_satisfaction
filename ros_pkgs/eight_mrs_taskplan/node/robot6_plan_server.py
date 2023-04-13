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


# robot 6
try:
    # geometry_name, agent_radius, agent_id, v_max, initial_position
    currentDir = '/home/hz/catkin_ws/src/eight_mrs_taskplan/node/results/'
    textfile6_d = open(currentDir + 'traj6d.txt', 'w')
    textfile6_a = open(currentDir + 'traj6a.txt', 'w')

    kepherarobot6 = KepRobot('ColumbusCirclePoly', 0.177, 5, 0.20, [0.5, 2.5],\
       '/tb3_5/cmd_vel', '/tb3_5/odom', [textfile6_d, textfile6_a], 0.05, [])

    kepherarobot6.task_server.start()

    rospy.spin()
    textfile6_d.close()
    textfile6_a.close()
except rospy.ROSInterruptException:
    pass

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
    currentDir = '/home/hz/catkin_ws/src/mrs_taskplan/node/results/'
    textfile3_d = open(currentDir + 'traj3d.txt', 'w')
    textfile3_a = open(currentDir + 'traj3a.txt', 'w')

    kepherarobot3 = KepRobot('ColumbusCirclePoly', 0.177, 2, 0.20, [3.5, 0.5],
                             '/tb3_2/cmd_vel', '/tb3_2/odom', [textfile3_d, textfile3_a], 0.05, [])

    kepherarobot3.task_server.start()

    rospy.spin()
    textfile3_d.close()
    textfile3_a.close()
except rospy.ROSInterruptException:
    pass

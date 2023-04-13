#! /usr/bin/env python

import rospy
import actionlib
from mrs_taskplan.msg import TaskAction, TaskGoal, TaskResult
from mrs_taskplan.msg import PlanindexAction, PlanindexGoal, PlanindexResult, PlanindexFeedback
from mrs_plan_client_class import Transition, Taskplan

"""First, construct four clients for all the (four) robots"""
# #####################################################
global keph0_task_client, keph1_task_client, keph2_task_client, keph3_task_client
global kephera_clients


""" If provided 4 robots """

tasklist2_2 = ['C', 'F']
transList2_2 = [Transition('C',[6]), Transition('F',[6])]
robotlist2_2 = 6
subeventList2_2 = [['C', 'F']]
taskplan2 = Taskplan(tasklist2_2, transList2_2, robotlist2_2, 2, subeventList2_2, 1)


try:
    rospy.init_node('taskplanning1', anonymous=True)

    taskplan2.send_goal()

    rospy.spin()
except rospy.ROSInterruptException:
    pass


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


""" If provided with 4 robots """

tasklist2_3 = ['B', 'E']
transList2_3 = [Transition('B', [7]), Transition('E', [5])]
robotlist2_3 = (7,5)
subeventList2_3 = [['B', 'E']]
taskplan2 = Taskplan(tasklist2_3, transList2_3, robotlist2_3, 3, subeventList2_3, 1)


try:
    rospy.init_node('taskplanning4', anonymous=True)

    taskplan2.send_goal()

    rospy.spin()
except rospy.ROSInterruptException:
    pass


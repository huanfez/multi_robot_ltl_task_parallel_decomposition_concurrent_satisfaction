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


# """ If provided 4 robots """
tasklist2_0 = ['c', 'f']
transList2_0 = [Transition('c',[2]), Transition('f',[0])]
robotlist2_0 = (2, 0)
subeventList2_0 = [['c', 'f']]
taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)


try:
    rospy.init_node('taskplanning1', anonymous=True)

    taskplan2.send_goal()

    rospy.spin()
except rospy.ROSInterruptException:
    pass


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


# """ If provided 2 robots """
tasklist2_1 = ['C', 'F', 'B', 'E']
transList2_1 = [Transition('C',[6]), Transition('F',[6]), Transition('B',[6]), Transition('E',[6])]
robotlist2_1 = 6
subeventList2_1 = [['C', 'F', 'B', 'E']]
taskplan2 = Taskplan(tasklist2_1, transList2_1, robotlist2_1, 1, subeventList2_1, 1)


try:
    rospy.init_node('taskplanning2', anonymous=True)

    taskplan2.send_goal()

    rospy.spin()
except rospy.ROSInterruptException:
    pass


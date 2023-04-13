#! /usr/bin/env python

import rospy
import actionlib
from mrs_taskplan.msg import TaskAction, TaskGoal, TaskResult
from mrs_taskplan.msg import PlanindexAction, PlanindexGoal, PlanindexResult, PlanindexFeedback
from mrs_plan_client_class import Transition, Taskplan

global keph0_task_client, keph1_task_client, keph2_task_client, keph3_task_client
global kephera_clients


""" If provided with 2 robots """

tasklist2_1 = ['b', 'e']
transList2_1 = [Transition('b', [3]), Transition('e', [1])]
robotlist2_1 = (3,1)
subeventList2_1 = [['b', 'e']]
taskplan2 = Taskplan(tasklist2_1, transList2_1, robotlist2_1, 1, subeventList2_1, 1)


try:
    rospy.init_node('taskplanning2', anonymous=True)

    taskplan2.send_goal()

    rospy.spin()
except rospy.ROSInterruptException:
    pass

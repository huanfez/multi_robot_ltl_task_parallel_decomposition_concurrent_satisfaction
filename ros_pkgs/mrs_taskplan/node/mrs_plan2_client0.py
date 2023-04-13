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


# task list: store a sequence of (event, rid): dictionary
# #####################################################
# # Experiment 1
# tasklist2_0 = ['a', 'f', 'e']
# transList2_0 = [Transition('a',[1]), Transition('f',[2]), Transition('e',[2])]
# robotlist2_0 = (1,2)
# subeventList2_0 = [['a', 'f', 'e']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)
#####################################################
# Experiment 2
tasklist1 = [('a', 'epslion'), ('b', 'epslion')]
transList1 = [Transition('a', [1]), Transition('b', [1])]
robotlist1 = 1
subeventList1 = [['a', 'b']]
taskplan1 = Taskplan(tasklist1, transList1, robotlist1, 0, subeventList1, 1)

##################################################################################################
# """ Parallel tasking"""
# """ If provided 1 robot """

# tasklist2_0 = ['c', 'f', 'b', 'e']
# transList2_0 = [Transition('c',[2]), Transition('f',[2]), Transition('b',[2]), Transition('e',[2])]
# robotlist2_0 = 2
# subeventList2_0 = [['c', 'f', 'b', 'e']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

# """ If provided 2 robots """
#
# tasklist2_0 = ['c', 'f']
# transList2_0 = [Transition('c',[2]), Transition('f',[2])]
# robotlist2_0 = 2
# subeventList2_0 = [['c', 'f']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)
#
# """ If provided with 4 robots """
#
# tasklist2_0 = ['c', 'f']
# transList2_0 = [Transition('c',[2]), Transition('f',[0])]
# robotlist2_0 = (2, 0)
# subeventList2_0 = [['c', 'f']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

########################################################################################
# """ If provided 2 robot serial tasking"""
#
# tasklist2_0 = ['c', 'f', 'b', 'e']
# transList2_0 = [Transition('c',[2]), Transition('f',[2]), Transition('b',[3]), Transition('e',[3])]
# robotlist2_0 = (2,3)
# subeventList2_0 = [['c', 'f', 'b', 'e']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

# """ If provided 4 robot serial tasking"""
#
# tasklist2_0 = ['c', 'f', 'b', 'e']
# transList2_0 = [Transition('c',[2]), Transition('f',[0]), Transition('b',[3]), Transition('e',[1])]
# robotlist2_0 = (2, 0, 3, 1)
# subeventList2_0 = [['c', 'f', 'b', 'e']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

try:
    rospy.init_node('taskplanning1', anonymous=True)

    taskplan1.send_goal()

    rospy.spin()
except rospy.ROSInterruptException:
    pass


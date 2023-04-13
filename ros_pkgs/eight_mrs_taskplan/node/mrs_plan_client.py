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


# # task list1: store a sequence of (event, rid): dictionary
# tasklist1 = [('a', 'epslion'), ('b', 'epslion'), ('c', 'epslion'), ('epslion', 'd'),
#              ('epslion', 'e'), ('epslion', 'f'), ('g', 'epslion')]
# transList1 = [Transition('a',[1]), Transition('b',[1]), Transition('c',[1])]
# #   Transition('d',[2]), Transition('e',[2]), Transition('f',[2]), \
# #   Transition('g',[1,2])]
# robotlist1 = (1,2)
# subeventList1 = [['a', 'b', 'c', 'd', 'e', 'f', 'g']]
# taskplan1 = Taskplan(tasklist1, transList1, robotlist1, 0, subeventList1, 0)

# task list2: store a sequence of (event, rid): dictionary
""" Parallel tasking"""
# """ If provided 2 robot """
#
# tasklist2_0 = ['c', 'f', 'b', 'e']
# transList2_0 = [Transition('c',[2]), Transition('f',[2]), Transition('b',[2]), Transition('e',[2])]
# robotlist2_0 = 2
# subeventList2_0 = [['c', 'f', 'b', 'e']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

# """ If provided 4 robots """
#
# tasklist2_0 = ['c', 'f']
# transList2_0 = [Transition('c',[2]), Transition('f',[2])]
# robotlist2_0 = 2
# subeventList2_0 = [['c', 'f']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

""" If provided with 8 robots """

tasklist2_0 = ['c', 'f']
transList2_0 = [Transition('c',[2]), Transition('f',[0])]
robotlist2_0 = (2, 0)
subeventList2_0 = [['c', 'f']]
taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

########################################################################################
# """ If provided 2 robot serial tasking"""

# tasklist2_0 = ['c', 'f', 'b', 'e', 'C', 'F', 'B', 'E']
# transList2_0 = [Transition('c',[2]), Transition('f',[2]), Transition('b',[2]), Transition('e',[2]), \
#                 Transition('C',[6]), Transition('F',[6]), Transition('B',[6]), Transition('E',[6])]
# robotlist2_0 = (2,6)
# subeventList2_0 = [['c', 'f', 'b', 'e', 'C', 'F', 'B', 'E']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

# """ If provided 4 robot serial tasking"""
#
# tasklist2_0 = ['c', 'f', 'b', 'e', 'C', 'F', 'B', 'E']
# transList2_0 = [Transition('c',[2]), Transition('f',[2]), Transition('b',[3]), Transition('e',[3]), \
#                 Transition('C',[6]), Transition('F',[6]), Transition('B',[7]), Transition('E',[7])]
# robotlist2_0 = (2,3,6,7)
# subeventList2_0 = [['c', 'f', 'b', 'e', 'C', 'F', 'B', 'E']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

# """ If provided 8 robot serial tasking"""

# tasklist2_0 = ['c', 'f', 'b', 'e', 'C', 'F', 'B', 'E']
# transList2_0 = [Transition('c',[2]), Transition('f',[0]), Transition('b',[3]), Transition('e',[1]), \
#                 Transition('C',[6]), Transition('F',[4]), Transition('B',[7]), Transition('E',[5])]
# robotlist2_0 = (2,0,3,1,6,4,7,5)
# subeventList2_0 = [['c', 'f', 'b', 'e', 'C', 'F', 'B', 'E']]
# taskplan2 = Taskplan(tasklist2_0, transList2_0, robotlist2_0, 0, subeventList2_0, 1)

try:
    rospy.init_node('taskplanning1', anonymous=True)

    taskplan2.send_goal()

    rospy.spin()
except rospy.ROSInterruptException:
    pass


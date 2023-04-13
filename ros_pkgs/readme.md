# Turtlebot3 ROS GAZEBO

Ubuntu18.0 
ROS Melodic 
Python2

_Directory_ ~/catkin_ws_hz/mrs_modelchecking

***
## Package1. mrs_turtlebot3

_Function_ launch robots and environment

_**one_turtlebot3.launch**_ set one turtlebot3

_**two_turtlebot3.launch**_ set two turtlebot3

_**four_turtlebot3.launch**_ set four turtlebot3

_**eight_turtlebot3.launch**_ set eight turtlebot3



***
## Package2.1. mrs_taskplan

(Two LTL task specifications in the simulation experiments)

_Function_: launch 'task plan sender' (send task one by one) and 'task plan server' (receive every task from the 'task plan sender' and launch an action: start moving from current position and stop at target position)

**Steps To Launch Experiment Case Study 1**

`$roslaunch mrs_turtlebot3 four_turtlebot3.launch`

`$roslaunch mrs_taskplan mrs_turtles_planer1.launch`

**Steps To Launch Experiment Case Study 2**

`$roslaunch mrs_turtlebot3 four_turtlebot3.launch`

`$roslaunch mrs_taskplan mrs_turtles_planer2_1.launch`


***
## Package2.2. eight_mrs_taskplan

(for the computational comparison: note there are many cases in the comparision table, we select the following representatives)

_Function_ launch task plan sender (send task one by one) and task plan server(receive every task and launch an action: start moving from current position and stop at target position). The amount of task plan sender is based on the `parallelism`.

_**mrs_z1_r1_1clients4tasks.launch**_  z=1, launch 1 task plan sender, launch 1 task plan servers (robots)

_**mrs_z1_r2_1clients4tasks.launch**_  z=1, launch 1 task plan sender, launch 2 task plan servers (robots)

_**mrs_z1_r4_1clients4tasks.launch**_  z=1, launch 1 task plan sender, launch 4 task plan servers (robots)

_**mrs_z2_r2_1clients8tasks.launch**_  z=2, launch 1 task plan sender, launch 2 task plan servers (robots)

_**mrs_z2_r4_1clients8tasks.launch**_  z=2, launch 1 task plan sender, launch 4 task plan servers (robots)

_**mrs_z2_r8_1clients8tasks.launch**_  z=2, launch 1 task plan sender, launch 8 task plan servers (robots)

----------------------------------------------------------------------------------------------------------

_**mrs_z1_r2_2clients4tasks.launch**_  z=1, launch 2 task plan sender, launch 2 task plan servers (robots)

_**mrs_z1_r4_2clients4tasks.launch**_  z=1, launch 2 task plan sender, launch 4 task plan servers (robots)

_**mrs_z2_r2_2clients8tasks.launch**_  z=2, launch 2 task plan sender, launch 2 task plan servers (robots)

_**mrs_z2_r4_4clients8tasks.launch**_  z=2, launch 4 task plan sender, launch 4 task plan servers (robots)

_**mrs_z2_r8_4clients8tasks.launch**_  z=2, launch 4 task plan sender, launch 8 task plan servers (robots)

**Examplary Steps To Launch the motion**

`$roslaunch mrs_turtlebot3 four_turtlebot3.launch` # The case is 4-robot. If the case is 2-robot, launch two_turtlebot3.launch instead etc. 

`$roslaunch eight_mrs_taskplan mrs_z1_r4_2clients4tasks.launch` # The case is z=1 (`z1`), 4-robot(`r4`), 2 parallelism(`2clients`)

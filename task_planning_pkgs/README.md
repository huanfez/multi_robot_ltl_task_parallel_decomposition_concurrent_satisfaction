# automata_decomposition_allocation

JAVA 8.0+

Eclipse

***
## 1. automaton parallel decomposition

_Directory_ ~/Documents/huanfei/task_planning_model_checker/Decomposition/dk/brics/automaton/* 
**-packages for automaton operation and iterative parallel decomposition**
A preliminary package for the `automaton-robot assignment based task planning` no implementation is needed

** YW: Use which software to run which codes?

***
## 2. automaton-robot assignment based task planning
**YW：directory should be ~/Documents/huanfei/task_planning_model_checker/TaskAllocAut/src/taskPlanning2 

_Directory_ TaskAllocAut/src/taskPlanning2:

_**Experiment:**_

Experiment_case1.java **- case 1**

Experiment_case2.java **- case 2**

**Steps to launch the program** 

(0) launch "Eclipse" IDE in the Application, and extend the "Project Explorer"->"TaskAllocAut"->"src"->"taskPlanning2" in the left panel of "Eclipse";

(1) e.g., if expect to get the results of case1, click "Experiment_case1.java" to show the code;

(2) Click the "debug" or "run" button on the top meanu of "Eclipse" to run the program and generate the results. Results are are shown in the "Console" of "Eclipse"

(3) Perform the same operations in (1) and (2) for a different file (the above .java file) if expect to obtain the results for different situation

--------------------------------------------------------

_**Computational Comparison with Centralized Method:**_

(Decentralized computation results)

ComptExperiment_Z1_Robot1.java 
**- assign 1 robot to 1 automaton**

ComptExperiment_Z1_Robot2.java 
**- assign 2 robots to 1 automaton**

ComptExperiment_Z1_Robot4.java 
**- assign 4 robots to 1 automaton**

ComptExperiment_Z2_Robot2.java
**- assign 2 robots to 2 automaton**

ComptExperiment_Z2_Robot4.java
**- assign 4 robots to 2 automaton**

ComptExperiment_Z2_Robot8.java 
**- assign 8 robots to 2 automaton**

ComptExperiment_Z2_Robot12.java 
**- assign 8 robots to 2 automaton**

ComptExperiment_Z3_Robot2.java 
**- assign 2 robots to 3 automaton**

ComptExperiment_Z3_Robot4.java 
**- assign 4 robots to 3 automaton**

ComptExperiment_Z3_Robot8.java 
**- assign 8 robots to 3 automaton**

ComptExperiment_Z3_Robot12.java
**- assign 12 robots to 3 automaton**

ComptExperiment_Z4_Robot2.java 
**- assign 2 robots to 4 automaton**

ComptExperiment_Z4_Robot4.java 
**- assign 4 robots to 4 automaton**

ComptExperiment_Z4_Robot8.java 
**- assign 8 robots to 4 automaton**

ComptExperiment_Z4_Robot12.java 
**- assign 12 robots to 4 automaton**

ComptExperiment_Z4_Robot16.java
**- assign 12 robots to 4 automaton**

-------------------------------------------

(Centralized computation results)

ComptExperiment_centralized_Z1_Robot2.java 
**- assign 2 robots to 1 automaton**

ComptExperiment_centralized_Z1_Robot4.java 
**- assign 4 robots to 1 automaton**

ComptExperiment_centralized_Z2_Robot2.java 
**- assign 2 robots to 2 automaton**

ComptExperiment_centralized_Z2_Robot4.java 
**- assign 4 robots to 2 automaton**

ComptExperiment_centralized_Z3_Robot2.java 
**- assign 2 robots to 3 automaton**

ComptExperiment_centralized_Z4_Robot2.java 
**- assign 2 robots to 4 automaton**

-------------------------------------------------
**Steps to launch the program** 

(0) launch "Eclipse" IDE in the Application, and extend the "Project Explorer"->"TaskAllocAut"->"src"->"taskPlanning2" in the left panel of "Eclipse";

(1) e.g., if expect to get the results of decentralized computation in the case of Z=2, robots = 4, click "ComptExperiment_Z2_Robot4.java" to show the code;

(2) Click the "debug" or "run" button on the top meanu of "Eclipse" to run the program and generate the 'automaton decomposition time' and 'task planning solution computation time'. The results are shown in the "Console" of "Eclipse"

(3) Perform the same operations in (1) and (2) for a different file (the above .java file) if expect to obtain the results for different situation

**See more for the computatinal results in DEDS paper**
![Table 3](https://gitlab.com/-/ide/project/i2r-research-group/smp/task-decomposition-and-allocation/automata_decomposition_allocation/tree/HZ/-/results/computational_results.png/)

Scheduling Algorithm Project by Muazzum Akhtar
CSCI 340 - Prof Rahman 

This python program implements the following 4 scheduling algorithms: 
- First Come, First Served FCFS
- Shortest Job First SJF
- Priority Scheduling PS
- Round Robin RR

Stores task set into a list and takes it as input. 
Keys are used to define the task set as follows:
     Task: string value carrying the name.
     Priority: an integer value which holds the priority number of each task.
     cpu_burst: integer that holds CPU burst time.
NOTE: Functions in program also use 'arrival-time' which notes the time of the task's arrival.

Each function prints out the average waiting time, average turnaround time, and the Gantt chart. 
Below is a brief overview of each scheduling algorithm.
     FCFS: 
        Executes tasks as they arrive. First come, first serve bases.
      SJF: 
         Whichever process has the smallest CPU burst time gets executed first.
         Any tie in burst time will get broken randomly.
      Priority Scheduling:
         A priority is assigned to each task. The smallest number priority will run first; however,
         if the processes has the same priority then we decide using the arrival time. 
      RR: 
         A time_quantum exists. In my program the time_quantum is 10 meaning the first process that arrives 
         will execute only to 10 cpu burst and then moves onto the next process in the queue. Any remaining time/bursts 
         are saved into a variable and only when each task is visited once do we go back to those 
         who hasn't completed yet. 

I had defined a function for each of the algorithms. 
Each function has the following:
     - variables initialized to track the waiting time, turnaround time, and current time.
     - a list that stores the start and end times for each tasks (for gantt chart)
     - a sorted task set that sorts the data by burst time, name, priority, or arrival time depending
     on the algorithm used.
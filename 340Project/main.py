# 340 Project by Muazzum Akhtar 

import random

# First Come First Serve 
def fcfs(task_set):
    # Sort the task set by the order of arrival (in this case, they all arrive at the same time)
    sorted_task_set = sorted(task_set, key=lambda task: task['task'])

    # Initialize variables for waiting time, turnaround time, and current time usde for averages
    waitTime = 0
    turnaround_time = 0
    currTime = 0
    
    # list initialize to hold start and end times of the tasks
    gantt_time = []

    # Iterate through each task in the sorted task set
    for task in sorted_task_set:
        # Add the waiting time for this task to the total waiting time
        waitTime += currTime

        # Calculate the turnaround time for this task and add it to the total turnaround time
        turnaround_time += currTime + task['cpu_burst']

        # append the start and end times to the list for the gantt chart presentation.
        gantt_time.append((task['task'], currTime, currTime + task['cpu_burst']))

        # Increment the current time by the burst time of this task
        currTime += task['cpu_burst']

    # Calculate the average waiting and turnaround time
    num_tasks = len(task_set)
    avg_waiting_time = waitTime / num_tasks
    avg_turnaround_time = turnaround_time / num_tasks

    # Results
    print("FCFS: ")
    # print the Gantt chart. If its not the last element in list then add comma.
    for i, task in enumerate(gantt_time):
        if i == len(gantt_time) - 1:
            print(f"{task[0]} [{task[1]} - {task[2]}]")
        else:
            print(f"{task[0]} [{task[1]} - {task[2]}]", end=", ")
    print("Avg. Waiting Time: ", avg_waiting_time)
    print("Avg. Turnaround Time: ", avg_turnaround_time)
    print()

# Define the task set
task_set = [
    {'task': 'T1', 'priority': 2, 'cpu_burst': 20},
    {'task': 'T2', 'priority': 4, 'cpu_burst': 25},
    {'task': 'T3', 'priority': 3, 'cpu_burst': 25},
    {'task': 'T4', 'priority': 3, 'cpu_burst': 15},
    {'task': 'T5', 'priority': 1, 'cpu_burst': 10}
]

# Call the FCFS function with the task set
fcfs(task_set)


# Shortest Job First Function
def sjf(task_set):
    sorted_task_set = sorted(task_set, key=lambda task: task['cpu_burst'])

    # Initialize variables for waiting time, turnaround time, and current time usde for averages
    currTime = 0
    waitTime = 0
    turnaround_time = 0
    # Holds start and end times for each process
    gantt_time = []

    # itterate through the task set and concurrently add onto the waiting time counter and turnaround time counter 
    # add the current time and current time + burst onto the gantt timeline for the start and end times
    for i, task in enumerate(sorted_task_set):
         waitTime += currTime
         turnaround_time += currTime + task['cpu_burst']
         gantt_time.append((task['task'], currTime, currTime + task['cpu_burst']))
         currTime += task['cpu_burst']

         # Randomly break ties if tasks has same burst time
         if i < len(sorted_task_set) - 1 and task['cpu_burst'] == sorted_task_set[i+1]['cpu_burst']:
            random.shuffle(sorted_task_set[i:i+2])

    # Calculate the average waiting and turnaround time
    num_tasks = len(task_set)
    avg_waiting_time = waitTime / num_tasks
    avg_turnaround_time = turnaround_time / num_tasks

    print("SJF: ")
    for i, task in enumerate(gantt_time):
        if i == len(gantt_time) - 1:
            print(f"{task[0]} [{task[1]} - {task[2]}]")
        else:
            print(f"{task[0]} [{task[1]} - {task[2]}]", end=", ")
    print("Avg. Waiting Time: ", avg_waiting_time)
    print("Avg. Turnaround Time: ", avg_turnaround_time)
    print()

# function call 
sjf(task_set)

# Priority Scheduling
def ps(task_set):
    
    # Firstly, setting a random arrival time from 0 to 100 to each task
    for task in task_set:
        task['arrival_time'] = random.randint(0,100)

    # sort data from task set by the task's priority and arrival time 
    sorted_task_set = sorted(task_set, key=lambda task: (task['priority'], task['arrival_time']))

    currTime = 0
    waitTime = 0
    turnaround_time = 0
    gantt_time = []

    for task in sorted_task_set:
        waitTime += currTime
        turnaround_time += currTime + task['cpu_burst'] - task['arrival_time']
        gantt_time.append((task['task'], currTime, currTime + task['cpu_burst']))
        currTime += task['cpu_burst']

    num_tasks = len(task_set)
    avg_waiting_time = waitTime / num_tasks
    avg_turnaround_time = turnaround_time / num_tasks

    print("Priority Scheduling: ")
    for i, task in enumerate(gantt_time):
        if i == len(gantt_time) - 1:
            print(f"{task[0]} [{task[1]} - {task[2]}]")
        else:
            print(f"{task[0]} [{task[1]} - {task[2]}]", end=", ")
    print("Avg. Waiting Time: ", avg_waiting_time)
    print("Avg. Turnaround Time: ", avg_turnaround_time)
    print()

# function call
ps(task_set)

# Round Robin
def rr(task_set, time_quantum):
    
    currTime = 0
    waitTime = 0
    turnaround_time = 0
    gantt_time = []
    remainingBurstTime = [task['cpu_burst'] for task in task_set]
    num_tasks = len(task_set)

    # Used while loop to keep looping through until there is no remaining burst time left. 
    while True:
        done = True
        
        # Keep going if there is still some burst time left 
        for i in range(num_tasks):
            if remainingBurstTime[i] > 0:
                done = False

                # update variables when burst time is greater than time quantum, append to gantt timeline 
                # and revisit later 
                if remainingBurstTime[i] > time_quantum:
                    currTime += time_quantum
                    remainingBurstTime[i] -= time_quantum
                    gantt_time.append((task_set[i]['task'], currTime - time_quantum, currTime))

                # If no burst time leftover update waiting and current time and append to gantt chart 
                # this process is now done executing
                else:
                    currTime += remainingBurstTime[i]
                    waitTime += currTime - task_set[i]['cpu_burst']
                    remainingBurstTime[i] = 0
                    turnaround_time += currTime
                    gantt_time.append((task_set[i]['task'], currTime - remainingBurstTime[i], currTime))

        if done == True:
            break
        
    avg_waiting_time = waitTime / num_tasks
    avg_turnaround_time = turnaround_time / num_tasks   

    print("Round Robin: ")
    for i, task in enumerate(gantt_time):
        if i == len(gantt_time) - 1:
            print(f"{task[0]} [{task[1]} - {task[2]}]")
        else:
            print(f"{task[0]} [{task[1]} - {task[2]}]", end=", ")
    print("Avg. Waiting Time: ", avg_waiting_time)
    print("Avg. Turnaround Time: ", avg_turnaround_time) 

# function call
rr(task_set, 10)
            

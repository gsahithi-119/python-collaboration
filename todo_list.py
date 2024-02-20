# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:27:19 2024

@author: gsahi
"""
tasklist = [] # create empty task list
# get user input
action = input("""What would you like to do? Press 
    a to add a tasks to the list
    v to view all tasks
    m to mark a task as completed
    d to delete a task
    s to sort tasks in alphabetical order
    >>> """)

# create function that numbers and prints all tasks in task list
def print_tasks(tasklist):
    num = 1
    for item in tasklist: # for each item
        print(str(num) + ".", tasklist[num-1]) # print numbering and item
        num += 1

# while user does not quit
while action != 'q':
    if action == 'v': # if action is view tasks
        print_tasks(tasklist) # print task list
   
    if action == 'a': # if action is to add tasks
        new = input("""What is the task you would like to add?
    >>> """) # get new task from user
        tasklist.append(new) # add task to task list
        print_tasks(tasklist) # print updated task list
        
    if action == 'd': # if action is to delete task
        # get the number of the task that user wants to delete    
        num = int(input("Which task would you like to delete? Enter the number >>> "))
        # delete that task, index is 1 less than the number user entered as index starts at 0
        tasklist.remove(tasklist[num-1]) 
        print_tasks(tasklist) # print updated task list
    
    if action == 'm': # if action is to mark task as completed
        # get the number of the task that user wants to mark     
        num = int(input("Which task would you like to mark as completed? Enter the number >>> "))
        completed = tasklist[num-1] + " ✓" # new variable that adds a checkmark to the task in list
        tasklist[num-1] = completed # update that task number to include checkmark
        print_tasks(tasklist) # print new list
    
    if action == 's':
        tasklist.sort()
        print_tasks(tasklist)
    
    if action == 'q': # if action is to quit
        break # leave for loop
    
    # get next action from user
    action = input("""What would you like to do? Press 
    a to add a tasks to the list
    v to view all tasks
    m to mark a task as completed
    d to delete a task
    s to sort tasks in alphabetical order
    q to quit
    >>> """)
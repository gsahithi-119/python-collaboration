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
    >>> """)

# create function that numbers and prints all tasks in task list
def print_tasks(tasklist):
    num = 1
    for item in tasklist:
        print(str(num) + ".", tasklist[num-1])
        num += 1

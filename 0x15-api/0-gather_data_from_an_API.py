#!/usr/bin/python3
'''Retrieves info from a RESTAPI using python'''
import requests
import sys


if len(sys.argv) > 1:
    e_id = sys.argv[1]
    e_id = int(e_id)

    # request for data
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    # print that info
    employees = users.json()
    tasks = todos.json()
    # find the employee's data
    for employee in employees:
        if employee['id'] == e_id:
            queried_user = employee['name']
    # tasks the user has completed
    complete_tasks = 0
    todo_list = []
    for task in tasks:
        if task["userId"] == e_id:
            todo_list.append(task)
            if task["completed"] is True:
                complete_tasks += 1
    # query the tasks:
    total_tasks = len(todo_list)
    print("Employee {} is done with tasks".format(queried_user) +
          "({}/{}):".format(complete_tasks, total_tasks))
    for item in todo_list:
        if item['completed'] is True:
            print("\t {}".format(item['title']))

#!/usr/bin/python3
'''Retrieves info from a RESTAPI using python'''
import json
import requests
import sys


# request for data
users = requests.get("https://jsonplaceholder.typicode.com/users")
todos = requests.get("https://jsonplaceholder.typicode.com/todos")

employees = users.json()
tasks = todos.json()

user_tasks = {}
# get the user id list
for employee in employees:
    e_id = employee['id']
    username = employee['username']
    # get task list for each user
    todo_list = []
    for task in tasks:
        values = {
            "username": "{}".format(username),
            "task": "{}".format(task['title']),
            "completed": "{}".format(task['completed']),
        }
        # list of dictionaries
        todo_list.append(values)
    # get the dictionary of list of dictionaries
    user_tasks[str(e_id)] = todo_list
# write json to file
json_object = json.dumps(user_tasks)
with open('todo_all_employees.json', 'w') as f:
    f.write(json_object)

#!/usr/bin/python3
'''Retrieves info from a RESTAPI using python'''
import json
import requests
import sys


# request for data
users = requests.get("https://jsonplaceholder.typicode.com/users").json()
tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()

user_tasks = {}
# get the user id list
for user in users:
    u_id = user['id']
    username = user['username']
    # get task list for each user
    todo_list = []
    for task in tasks:
        values = {
            "username": username,
            "task": task.get('title'),
            "completed": task['completed'],
        }
        # list of dictionaries
        todo_list.append(values)
    # get the dictionary of list of dictionaries
    user_tasks[str(u_id)] = todo_list
# write json to file
with open('todo_all_employees.json', 'w') as f:
    json.dump(user_tasks, f)

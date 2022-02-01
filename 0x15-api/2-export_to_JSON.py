#!/usr/bin/python3
'''Retrieves info from a RESTAPI using python'''
import json
import requests
import sys


if len(sys.argv) > 1:
    e_id = sys.argv[1]
    e_id = int(e_id)

    # request for data
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    employees = users.json()
    tasks = todos.json()
    # find the employee's data
    for employee in employees:
        if employee['id'] == e_id:
            queried_user = employee['username']
    # creating a list of the users task
    todo_list = []
    for task in tasks:
        if task["userId"] == e_id:
            values = {
                "task": "{}".format(task['title']),
                "completed": task['completed'],
                "username": "{}".format(queried_user)
            }
            todo_list.append(values)
    # creating dictionary containing user id and the tasks assigned to the user
    task_dict = {
        "{}".format(e_id): todo_list
    }
    # convert the above dcitionary to json object
    json_object = json.dumps(task_dict)
    # write json object to file
    with open("{}.json".format(e_id), "w") as f:
        f.write(json_object)

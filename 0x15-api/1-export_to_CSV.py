#!/usr/bin/python3
'''Retrieves info from a RESTAPI using python'''
import csv
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
            queried_user = employee['username']
    # tasks the user has completed
    complete_tasks = 0
    todo_list = []
    with open('{}.csv'.format(e_id), 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        for task in tasks:
            if task["userId"] == e_id:
                row = ['{}'.format(e_id),
                       '{}'.format(queried_user),
                       '{}'.format(task['completed']),
                       '{}'.format(task['title'])]
                writer.writerow(row)

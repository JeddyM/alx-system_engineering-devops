#!/usr/bin/python3
'''script that, using REST API, records all tasks from all employees
returns information in a json file
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: todo_all_employees.json
'''

import json
import requests
import sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'

    # convert into json to get a dictionary and list
    users = requests.get(url + "users").json()
    todos = requests.get(url + "users/{}/todos").json()
    username = user.get('username')

    # get list for a user
    user_tasks = []
    for task in todos:
        user_task.append(
                )
    # open file in write mode and write content
    with open("todo_all_employees.json", 'w', newline='') as jsonfile:
        json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                } for task in todos]}, jsonfile)

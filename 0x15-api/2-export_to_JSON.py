#!/usr/bin/python3
'''script that, using REST API, for a given employee ID
returns information in a csv file
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
'''

import json
import requests
import sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    # convert into json to get a dictionary and list
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(sys.argv[1])).json()
    username = user.get('username')

    # open file in write mode and write content
    with open("{}.json".format(user_id), 'w', newline='') as jsonfile:
        for task in todos:
            json.dump({user_id: [{
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                    }]}, jsonfile
                    )

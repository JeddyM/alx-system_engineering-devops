#!/usr/bin/python3
'''script that, using REST API, for a given employee ID
returns information in a csv file
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
'''
from csv import writer, QUOTE_ALL
import requests
import sys


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    # convert into json to get a dictionary and list
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(sys.argv[1])).json()
    username = user.get('name')

    # open file in write mode and write content
    with open("{}.csv".format(user_id), 'w', newline='', encoding='utf8') as f:
        task_writer = writer(f, quoting=QUOTE_ALL)
        for task in todos:
            task_writer.writerow([user_id, username, task.
                                  get("completed"), task.get("title")])

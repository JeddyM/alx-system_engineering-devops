#!/usr/bin/python3
import requests
import sys
'''script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
'''


if __name__ == "__main__":

    url = 'https://jsonplaceholder.typicode.com/'
    completed = []

    # convert into json to get a dictionary and list
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(sys.argv[1])).json()

    # print first line
    for task in todos:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed), len(todos)))

    # print titles
    for i in completed:
        print("\t {}".format(i))

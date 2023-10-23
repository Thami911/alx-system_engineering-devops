#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    user_Id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_Id))

    name = user.json().get('name')

    to_do = requests.get('https://jsonplaceholder.typicode.com/todos')
    total_Tasks = 0
    completed = 0

    for task in to_do.json():
        if task.get('userId') == int(user_Id):
            total_Tasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, total_Tasks))

    print('\n'.join(["\t " + task.get('title') for task in to_do.json()
          if task.get('userId') == int(user_Id) and task.get('completed')]))

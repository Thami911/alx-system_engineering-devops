#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos')
    to_do = to_do.json()

    todo_User = {}
    taskList = []

    for task in to_do:
        if task.get('userId') == int(user_Id):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todo_User[user_Id] = taskList

    filename = user_Id + '.json'
    with open(filename, mode='w') as f:
        json.dump(todo_User, f)

#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos')
    to_do = to_do.json()
    todo_All = {}

    for user in users:
        taskList = []
        for task in to_do:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todo_All[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_All, f)

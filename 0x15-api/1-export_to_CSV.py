#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    user_Id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_Id))
    name = user.json().get('username')
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = user_Id + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in to_do.json():
            if task.get('userId') == int(user_Id):
                writer.writerow([user_Id, name, str(task.get('completed')),
                                 task.get('title')])

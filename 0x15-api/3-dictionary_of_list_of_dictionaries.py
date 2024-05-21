#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 ''.format(user_id))

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    username = user_response.json().get('username')
    todos = todos_response.json()

    user_tasks = {user_id: []}

    for task in todos:
        user_tasks[user_id].append({
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
        })

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(user_tasks, jsonfile)

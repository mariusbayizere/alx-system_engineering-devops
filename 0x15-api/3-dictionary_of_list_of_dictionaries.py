#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    all_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    tasks_dict = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in all_todo if task.get("userId") == user.get("id")
        ]
        tasks_dict[user_id] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)

#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee
    and export it in CSV format.
"""
import csv
import requests
import sys


def export_employee_todo_to_csv(employee_id):
    """
    Fetch and export the TODO list progress for a given employee in CSV format.

    Args:
        employee_id (int): The ID of the employee
    """
    url = 'https://jsonplaceholder.typicode.com/'

    # Fetch employee data
    user_url = '{}users/{}'.format(url, employee_id)
    user_response = requests.get(user_url)
    user = user_response.json()
    username = user.get('username')

    # Fetch TODO list data for the employee
    todos_url = '{}todos?userId={}'.format(url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Open CSV file for writing
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username, task.get('completed'),
                             task.get('title')])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    export_employee_todo_to_csv(employee_id)

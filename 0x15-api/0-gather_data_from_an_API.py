#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee
    """
    url = 'https://jsonplaceholder.typicode.com/'

    # Fetch employee data
    user_url = '{}users/{}'.format(url, employee_id)
    user_response = requests.get(user_url)
    user = user_response.json()
    employee_name = user.get('name')

    # Fetch TODO list data for the employee
    todos_url = '{}todos?userId={}'.format(url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the employee TODO list progress
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

#!/usr/bin/python3
""" returns information about his/her TODO list progress """
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = r.json()
    for user in users:
        if user.get('id') == int(argv[1]):
            user_name = user.get('name')
            user_id = user.get('id')
            break

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = r.json()

    total_tasks = 0
    completed = 0
    tasks = []

    for todo in todos:
        if todo.get('userId') == user_id:
            total_tasks += 1
            if todo.get('completed') is True:
                completed += 1
                tasks.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        user_name,
        completed,
        total_tasks)
    )
    for task in tasks:
        print("\t "+task)

#!/usr/bin/python3
'''returns information about his/her TODO list progress'''
import csv
import requests
import sys


def get_info(resource, params=None):
    '''get the the data from API'''
    url = 'https://jsonplaceholder.typicode.com/' + resource
    if params:
        url += ('?' + params[0] + '=' + params[1])
    req = requests.get(url)
    return req.json()


if __name__ == '__main__':
    usr = get_info('users', ['id', sys.argv[1]])
    todos = get_info('todos', ['userId', sys.argv[1]])
    tasks_formated = []
    csv_file = 'USER_ID.csv'
    for k in todos:
        tasks_formated.append(
            [sys.argv[1], usr[0]['username'], k["completed"], k['title']])
    with open(csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(tasks_formated)

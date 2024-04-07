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
    csv_file = '{}.csv'.format(sys.argv[1])
    for k in todos:
        tasks_formated.append(
            [sys.argv[1], usr[0]['username'], k["completed"], k['title']])
    with open(csv_file, mode='w') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks_formated:
            writer.writerow([task[0],
                            task[1],
                            task[2],
                            task[3]])

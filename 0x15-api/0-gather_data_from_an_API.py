#!/usr/bin/python3
'''returns information about his/her TODO list progress'''
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
    tasks_completed = [task for task in todos if task['completed']]
    print('Employee {} is done with tasks({}/{}):'.format(usr[0]['name'],
                                                          len(tasks_completed),
                                                          len(todos)))
    for task in tasks_completed:
        print('\t {}'.format(task['title']))

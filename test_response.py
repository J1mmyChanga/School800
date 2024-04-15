from datetime import date

import requests

url = 'http://127.0.0.1:8080/api/tasks'
myobj = {'task': 'feesEFsF',
        'start': f'{date(year=2024, month=3, day=8)}',
        'end': f'{date(year=2024, month=3, day=10)}',
        'difficulty': 2,
        'completed': False,
        'type': 1,
        'kind': 3,
        'daily': 0}

myobj1 = {
        'id': 4
}

#print(requests.get(url))
#print(requests.post(url, json=myobj))
# print(requests.put(url, json=myobj1))
print(requests.put('http://127.0.0.1:8080//api/groups', json={'id': 3, 'rating': 464}))
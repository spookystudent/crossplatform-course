import requests


print(requests.post('http://127.0.0.1:5000/auth/login/', json={'name':'blackevildragon'}).json())
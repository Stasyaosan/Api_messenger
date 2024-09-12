import requests

url = 'http://127.0.0.1:8000/api/get_chats'
a = {'id_user': 5}
x = requests.post(url, data = a)

print(x.text)
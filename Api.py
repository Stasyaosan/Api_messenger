import requests
import config
import json


class Api:
    def __init__(self, token):
        self.token = token

    def request_post(self, method, params):
        url = f'{config.url}{method}'
        params['token'] = self.token
        if params != None:
            data = requests.post(url, data=params)
        else:
            data = requests.post(url)

        return data.text


class Auth:
    def init(self, login, password):
        self.login = login
        self.password = password

    def get_token(self):
        url = f'{config.URL}auth/'
        token = requests.post(url, data={'login': self.login, 'password': self.password})
        return json.loads(token.text)


token = Auth('qwe@qwe.ru', 'qwe@qwe.ru').get_token()
api = Api(token['token'])
print(api.request_post('get_chats', {'id_user': 13}))

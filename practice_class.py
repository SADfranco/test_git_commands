import json
import requests


class Test:

    def __init__(self, url):
        self.url = url

    def request(self, request):
        res = requests.get(f'{self.url}/search/?text={request}')
        c=1
        return print(res.text)


test = Test('https://ya.ru')
test.request('погода в москве')

import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
}

proxyDict = {
    "http": "http://222.208.80.142:9000"
}


def fetch_text(url):
    r = requests.get(url, headers=headers)
    print('url:{}'.format(r.request.url))
    r.encoding = 'utf-8'
    return r.text


def print_obj(obj):
    print(json.dumps(obj, default=lambda obj: obj.to_json, ensure_ascii=False))

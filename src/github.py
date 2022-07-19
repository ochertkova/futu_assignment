import json
import requests

serviceurl = "https://api.github.com/"

headers = {
    'User-Agent': 'ochertkova/futu_assignment'
}

cache = dict()

def get_user(username):
    if username in cache.keys():
        return cache[username]
    r = requests.get('https://api.github.com/users/{}'.format(username), headers)
    if r.status_code == 200:
        user_resp = r.json()
        repos = requests.get(user_resp['repos_url'], headers)
        user_resp['repos'] = repos.json()
        cache[username] = user_resp
        return user_resp
    else:
        return None

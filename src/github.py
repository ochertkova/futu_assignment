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

def get_repo(owner, reponame):
    if reponame in cache.keys():
        return cache[reponame]
    r = requests.get('https://api.github.com/repos/{}/{}'.format(owner,reponame), headers)
    if r.status_code == 200:
        repo_resp = r.json()
        languages = requests.get(repo_resp['languages_url'], headers)
        repo_resp['languages'] = languages.json()
        cache[reponame] = repo_resp
        return repo_resp
    else:
        return None

    

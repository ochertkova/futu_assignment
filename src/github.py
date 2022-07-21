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
        cache[reponame] = repo_resp
        return repo_resp
    else:
        return None

def fav_languages(username):
    user = get_user(username)
    fav_lang_dict = {}
    if user:
        for r in user['repos']:
            if r['language'] not in fav_lang_dict:
                fav_lang_dict[r['language']] = 0
            fav_lang_dict[r['language']] += 1
    return fav_lang_dict

    

import json
import requests

serviceurl = "https://api.github.com/"

headers = {
    'User-Agent': 'ochertkova/futu_assignment'
}

cache = dict()

def get_user(username):
    """Get user info as a dictionary
       Get repos info into user dictionary under 'repos' key
       Build cache dictionary for user to avoid GitHub rate limit problems
       Error case is not being handled well yet. #TODO: write a function processing status codes and rate limit
    """
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
    """Get repo info as a dictionary
       Get languages info into user dictionary under 'repos' key
       Build cache dictionary for repo to avoid GitHub rate limit problems
       Error case is not being handled well yet. #TODO: write a function processing status codes and rate limit
    """
    cache_key = ('{}/{}'.format(owner,reponame)) #store repo in cache as owner/reponame

    if cache_key in cache.keys():
        return cache[cache_key]
    r = requests.get('https://api.github.com/repos/{}/{}'.format(owner,reponame), headers)
    if r.status_code == 200:
        repo_resp = r.json()
        languages = requests.get(repo_resp['languages_url'], headers)
        repo_resp['languages'] = languages.json()
        cache[cache_key] = repo_resp
        return repo_resp
    else:
        return None

    

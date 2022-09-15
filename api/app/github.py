import requests
import app.settings as settings
import os

if not os.path.exists(f'./app/{settings.REPO}.git'):
    os.chdir('./app')
    os.system(f'git clone --bare https://github.com/{settings.CREATOR}/{settings.REPO}.git')
    os.chdir(f'./{settings.REPO}.git')
else:
    os.chdir(f'./app/{settings.REPO}.git')

###############################
###### Github API calls #######
###############################

# gets the github token straight from github given a gh access code
def get_token(code):
    url = 'https://github.com/login/oauth/access_token'
    myobj = {
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'code' : code,
        'redirect_uri' : settings.REDIRECT_URI
    }
    gh_tok = requests.post(url, json = myobj)
    gh_tok = (gh_tok.text.split('&')[0].split('=')[1])
    return gh_tok

# gets the user info from github through the github API
def get_user(gh_token:str):
    return jwt_get(gh_token,'https://api.github.com/user')


star = f'https://api.github.com/user/starred/{settings.CREATOR}/{settings.REPO}'
def is_starred(token):
    resp = jwt_get(token,star,raw=True)
    return 204 == resp.status_code
    
def star_if_not(token):
    resp = jwt_get(token,star,raw=True)
    if 204 != resp.status_code:
        jwt_put(token,star,raw=True)

# hits our dbs first
# if the person exists, hit github
# TODO what about username changes ???
# Ignore them.
def get_mentor_candidate(token,username):
    return jwt_get(token,f'https://api.github.com/users/{username}')

################################################
########## Generic Helper Functions ############
################################################

def jwt_get(token, url, raw=False):
    headers={'Authorization': f'token {token}'}
    if raw:
        return requests.get(url,headers=headers)
    return requests.get(url,headers=headers).json()

def jwt_put(token, url, raw=False):
    headers={'Authorization': f'token {token}'}
    if raw:
        return requests.put(url,headers=headers)
    return requests.put(url,headers=headers).json()

def fetch():
    os.popen('git fetch --all')

def get_contributors():
    out = os.popen('git shortlog -sn --group=author --group=trailer:co-authored-by --all -e').read()
    out = out.replace('\t','\n').split('\n')
    conts = {}
    for i in range(0,len(out)-1,2):
        n,id = out[i],out[i+1]
        em = id.split('<')[1].split('>')[0]
        conts[em] = int(n)
    return conts
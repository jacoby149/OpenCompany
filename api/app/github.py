import requests
import app.settings as settings


###############################
###### Github API calls #######
###############################

# gets the github token straight from github given a gh access code
def get_token(code):
    url = 'https://github.com/login/oauth/access_token'
    print("CODE : ",code)
    myobj = {
        'client_id': settings.client_id,
        'client_secret': settings.client_secret,
        'code' : code,
        'redirect_uri' : "http://ui.localhost/"
    }
    gh_tok = requests.post(url, json = myobj)
    gh_tok = (gh_tok.text.split("&")[0].split("=")[1])
    return gh_tok

# gets the user info from github through the github API
def get_user(gh_token:str):
    return jwt_get(gh_token,"https://api.github.com/user")


star = "https://api.github.com/user/starred/jacoby149/web10"
def star_if_not(token):
    resp = jwt_get(token,star)
    if 204 != resp.status_code:
        jwt_put(token,star)

################################################
########## Generic Helper Functions ############
################################################

def jwt_get(token, url):
    headers={'Authorization': f'token {token}'}
    return requests.get(url,headers=headers).json()

def jwt_put(token, url):
    headers={'Authorization': f'token {token}'}
    return requests.put(url,headers=headers).json()

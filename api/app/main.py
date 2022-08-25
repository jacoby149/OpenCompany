import app.settings as settings
# import app.docs as docs
# import app.models as models
# import app.exceptions as exceptions

# import app.mongo as db
# import app.twilio as mobile
# import app.stripe as pay

###################################
######## Github Oauth Flow ########
###################################

import json
from fastapi import FastAPI
from starlette.config import Config
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
import requests



app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!secret")

config = Config('.env')
oauth = OAuth(config)

@app.get('/mono')
async def homepage(request: Request,code:str=None):
    token = request.session.get('token')

    # log in
    if not token and not code:
        url = f'https://github.com/login/oauth/authorize?client_id={settings.client_id}'
        return HTMLResponse(f'<a href="{url}">login</a>')

    # put token in
    if not token and code:
        request.session['token'] = get_token(code)
        token = request.session.get('token')

    user = api_call(token,"https://api.github.com/user")
    user_info = ""
    for k,v in user.items():
        user_info = user_info + f'{k}:{v}<br>'
    return HTMLResponse(f'{user_info}<a href="/logout">logout</a>')

def api_call(token, url):
    headers={'Authorization': f'token {token}'}
    return requests.get(url,headers=headers).json()

def get_token(code):
    url = 'https://github.com/login/oauth/access_token'
    myobj = {
        'client_id': settings.client_id,
        'client_secret': settings.client_secret,
        'code' : code,
        'redirect_uri' : "http://api.localhost/"
    }
    x = requests.post(url, json = myobj)
    return (x.text.split("&")[0].split("=")[1])

def get_user_info():
    # https://api.github.com/user
    pass

@app.get('/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

##################################
####### Ranking Promoting ########
##################################

# template endpoint
# @app.post("/manage_business",include_in_schema=False)
# async def manage_business(token: models.Token):
#     check_admin(token)    
#     username = decode_token(token.token).username
#     bus_id = mget_business_id(username)
#     return pay.create_business_session(bus_id)
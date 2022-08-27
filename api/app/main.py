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
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
import requests
import jwt



app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="!secret")
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

config = Config('.env')
oauth = OAuth(config)

@app.get('/login_url')
async def login_url():
    return f'https://github.com/login/oauth/authorize?client_id={settings.client_id}'

@app.get('/get_token')
def code_for_token(code:str):
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
    id = get_user_info(gh_tok)
    id["token"] = gh_tok
    return jwt.encode(id,settings.PRIVATE_KEY, algorithm=settings.ALGORITHM)

@app.get('/user_info')
def get_user_info(gh_token:str):
    return get(gh_token,"https://api.github.com/user")

def get(token, url):
    headers={'Authorization': f'token {token}'}
    return requests.get(url,headers=headers).json()

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
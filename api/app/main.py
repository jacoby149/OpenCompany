from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import jwt

import app.settings as settings
import app.github as github
import app.mongo as db
import app.rank as rank

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ranks')
async def get_ranks():
    return rank.ranks

@app.get('/login_url')
async def login_url():
    """
        gets the url for logging in
    """
    return f'https://github.com/login/oauth/authorize?client_id={settings.client_id}'

@app.get('/login')
def login(code:str):
    """
        get the github token,
        then get the db information
        then make the web10-network token from the gh token
    """
    gh_tok = github.get_token(code)
    gh_data = github.get_user(gh_tok)
    user = iget_user(gh_data)
    user.update(gh_data)
    user["token"] = gh_tok
    return jwt.encode(user,settings.PRIVATE_KEY, algorithm=settings.ALGORITHM)

@app.get('/contribution')
def contribution():
    return github.get_contributors()

# gets the user, inits then gets user if user doesn't exist 
def iget_user(gh_data):
    username = gh_data["login"]
    user = db.get_user(username)
    if not user:
        db.init_user({"login":username})
        user = db.get_user(username)
    del user['_id']
    return user

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
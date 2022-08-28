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
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import jwt

import app.github as github

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/login_url')
async def login_url():
    """
        gets the url for logging in
    """
    return f'https://github.com/login/oauth/authorize?client_id={settings.client_id}'

@app.get('/get_token')
def code_for_token(code:str):
    """
        get the github token,
        then make the web10-network token from the gh token
    """
    gh_tok = github.get_token(code)
    id = github.get_user(gh_tok)
    id["token"] = gh_tok
    return jwt.encode(id,settings.PRIVATE_KEY, algorithm=settings.ALGORITHM)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
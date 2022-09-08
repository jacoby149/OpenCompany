from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import jwt

import app.settings as settings
import app.github as github
import app.mongo as db
import app.rank as rank
import app.models as models

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

@app.get('/contributors')
def contribution():
    return github.get_contributors()

# gets the user, inits then gets user if user doesn't exist 
def iget_user(gh_data):
    node_id = gh_data["node_id"]
    login = gh_data["login"]
    user = db.get_user(node_id)
    if not user:
        # login is included purely for debugging
        db.init_user({"node_id":node_id,"login":login})
        user = db.get_user(node_id)
    del user['_id']
    return user

# checks if a mentor is a valid mentor, and returns the mentor if it is.
@app.post('/mentor')
def get_mentor_candidate(mentor_form:models.MentorForm):
    mentor = github.get_mentor_candidate(mentor_form.gh_tok, mentor_form.mentor_username)
    if "node_id" not in mentor:
        return {"rank":0}
    mentor_record = db.get_user(mentor["node_id"])
    if not mentor_record :
        mentor.update({"rank":0})
    else : 
        mentor.update({"rank":mentor_record["rank"]})
    return mentor

#TODO
@app.get('/promote')
def promote(mentor_form:models.MentorForm):
    print("heehee")
    pass

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
import app.settings as settings
import app.docs as docs
import app.models as models
import app.exceptions as exceptions

# interfaces
import app.mongo as db
import app.twilio as mobile
import app.stripe as pay


#############################################
########### APP INITIALIZATION ##############
#############################################

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI(
    title="web10",
    openapi_tags=docs.tags_metadata,
    description=docs.description,
    version="10.0.0.0",
    terms_of_service="http://example.com/terms/",
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


####################################################
################## Handle 422s #####################
####################################################

import logging
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


###################################
######## Github Oauth Flow ########
###################################

from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

config = Config('.env')  # read config from .env file
oauth = OAuth(config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret-string")

@app.route('/login')
async def login(request: Request):
    # absolute url for callback
    # we will define it below
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.route('/auth')
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    # <=0.15
    # user = await oauth.google.parse_id_token(request, token)
    user = token['userinfo']
    return user


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
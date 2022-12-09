import os

# github api credentials
CLIENT_ID="..."
CLIENT_SECRET="...."

# our api credentials
ALGORITHM = "HS256"
PRIVATE_KEY = "..."
DB_URL = "mongodb+srv://..."
DB="network"
PAY = False
AUTO_STAR = False
CREATOR="jacoby149"
REPO="web10"
REDIRECT_URI = "http://ui.localhost"

# goes through the above config variables 
# checks if env vars of those names exist and sets them if they do
vars = [v for v in globals()]
for v in vars :
    env_val = os.getenv(v)
    if env_val == None:
        continue
    else:
        globals()[v] = env_val
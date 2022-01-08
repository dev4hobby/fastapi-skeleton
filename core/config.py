import os
from dotenv import load_dotenv

load_dotenv('./.env')

PORT = os.environ['PORT']
SECRET_KEY = os.environ['SECRET_KEY']

# database settings
DATABASE_URL = (
    f"postgres://{os.environ['POSTGRES_USER']}:"
    f"{os.environ['POSTGRES_PASSWORD']}@"
    f"{os.environ['POSTGRES_HOST']}:"
    f"{os.environ['POSTGRES_PORT']}/"
    f"{os.environ['POSTGRES_DB']}"
)
APPS_MODELS = [
    "app.auth.models",
    "app.social_account.models",
    "app.user.models",
    "aerich.models",
]

# settings for jwt authentication
TOKEN_TYPE = os.environ['TOKEN_TYPE']
ALGORITHM = os.environ['ALGORITHM']
ACCESS_TOKEN_JWT_SUBJECT = os.environ['ACCESS_TOKEN_JWT_SUBJECT']
# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

# settings for smtp
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

# superuser settings
USERNAME_SUPERUSER = os.environ['SUPERUSER_NAME']
EMAIL_SUPERUSER = os.environ['SUPERUSER_EMAIL']
PASSWORD_SUPERUSER = os.environ['SUPERUSER_PASSWORD']
REPEAT_PASSWORD_SUPERUSER = os.environ['SUPERUSER_REPEAT_PASSWORD']

# git hub
CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']

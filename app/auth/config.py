from authlib.integrations.starlette_client import OAuth

from core.config import CLIENT_SECRET, CLIENT_ID, PORT

social_auth = OAuth()

redirect_uri = f"http://localhost:{PORT}/auth/github/callback"

social_auth.register(
    name="github",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "user"},
)

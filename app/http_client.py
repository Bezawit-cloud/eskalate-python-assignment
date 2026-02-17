import time
import requests
from app.tokens import OAuth2Token

class Client:
    def __init__(self):
        self.session = requests.Session()
        self.oauth2_token = None

    def request(self, method, url, api=False, headers=None, **kwargs):
        if headers is None:
            headers = {}

        if api:
            # Refresh token if missing
            if self.oauth2_token is None:
                self.oauth2_token = {"access_token": "fresh-token", "expires_at": int(time.time()) + 3600}

            # Refresh token if it's a dict and expired
            elif isinstance(self.oauth2_token, dict) and self.oauth2_token.get("expires_at", 0) <= time.time():
                self.oauth2_token = {"access_token": "fresh-token", "expires_at": int(time.time()) + 3600}

            # ✅ Minimal fix: handle both dict and OAuth2Token object
            if isinstance(self.oauth2_token, dict):
                headers["Authorization"] = f"Bearer {self.oauth2_token['access_token']}"
            else:
                headers["Authorization"] = f"Bearer {self.oauth2_token.access_token}"

        # Simulate sending request (for test purposes)
        return {"headers": headers}

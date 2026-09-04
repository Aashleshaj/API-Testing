import requests
import pytest
import os
from conftest import auth_token
from pathlib import Path
from dotenv import load_dotenv
script_dir = Path(__file__).parent
env_path = script_dir.parent / ".env"
# Load with the explicit path
load_dotenv(dotenv_path=env_path) # Load environment variables from .env file

BASE_URL = os.getenv("BASE_URL") 

class TestGetUserProfile:
    BASE_URL = BASE_URL + "/auth/me"

    def test_get_user_profile(self, auth_token):
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.get(self.BASE_URL, headers=headers)
        assert response.status_code == 200
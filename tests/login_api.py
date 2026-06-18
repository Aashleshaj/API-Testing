import requests
import pytest
import os
from pathlib import Path
from dotenv import load_dotenv
script_dir = Path(__file__).parent
env_path = script_dir.parent / ".env"


# Load with the explicit path
load_dotenv(dotenv_path=env_path) # Load environment variables from .env file

class TestLoginAPI:
    BASE_URL = os.getenv("BASE_URL") + "/auth/login"
    def test_get_user_profile(self):
        headers = { 
            "Content-Type": "application/json"
        }
        payload = {
            "username": "emilys",
            "password": "emilyspass"
        }   
        response = requests.post(self.BASE_URL, json=payload, headers=headers)
        assert response.status_code == 200
        Access_Token = response.json().get("accessToken")
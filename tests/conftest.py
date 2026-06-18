import pytest
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# Load env vars once for the whole session
script_dir = Path(__file__).parent
env_path = script_dir.parent / ".env"
load_dotenv(dotenv_path=env_path)

@pytest.fixture(scope="session")
def auth_token():
    """Logs in once per test session and returns the access token."""
    base_url = os.getenv("BASE_URL")
    login_url = f"{base_url}/auth/login"
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }
    
    response = requests.post(login_url, json=payload, headers=headers)
    
    # Fails the whole test suite immediately if login breaks
    response.raise_for_status() 
    
    return response.json().get("accessToken")
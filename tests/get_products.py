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

class TestGetProducts:
    BASE_URL = BASE_URL + "/products"

    def test_get_products(self,auth_token):
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        response = requests.get(self.BASE_URL, headers=headers)
        assert response.status_code == 200
        product_id = response.json().get("products")[0].get("id")
        BASE_URL1 = f"{self.BASE_URL}/{product_id}"
        response1 = requests.get(BASE_URL1, headers=headers)
        assert response1.status_code == 200
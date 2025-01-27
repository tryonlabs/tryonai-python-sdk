import os

import requests

def get_access_token(email: str, password: str):
    """
    Get an access token.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        str: The access token.
    """
    try:
        url = os.getenv("TRYONAI_SERVER_URL") + "/api/v1/user/token/"
        response = requests.post(url, data={"email": email, "password": password})
        if response.status_code != 200:
            raise Exception(f"Failed to get access token: {response.status_code} {response.text}")
        else:
            access_token = response.json()["access"]
            return access_token
    except Exception as e:
        raise Exception(f"Failed to get access token: {e}")

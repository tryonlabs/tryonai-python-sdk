import os

import requests

def upload_image(image_path: str, data: dict):
    """
    Upload an image.

    Args:
        image_path (str): The path to the image to be uploaded.
        data (dict): The data to be sent to the server.

    Raises:
        Exception: If the image upload fails.
        Exception: If the server returns an error.

    Returns:
        dict: The response from the server.
    """
    try:
        url = os.getenv("TRYONAI_SERVER_URL") + "/api/v1/experiment_image/"
        headers = {
            "Authorization": f"Bearer {os.getenv('TRYONAI_ACCESS_TOKEN')}",
        }

        files = {"image": open(image_path, "rb")}
        response = requests.post(url, headers=headers, files=files, data=data)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create experiment image: {response.text}")
    except Exception as e:
        raise Exception(f"Failed to create experiment: {e}")  


def create_experiment(**kwargs: dict):
    """
    Create an experiment.

    Args:
        **kwargs (dict): The data to be sent to the server.
        
    Raises:
        Exception: If the experiment creation fails.    
        Exception: If the server returns an error.

    Returns:
        dict: The response from the server.
    """
    try:
        url = os.getenv("TRYONAI_SERVER_URL") + "/api/v1/experiment/"
        headers = {
            "Authorization": f"Bearer {os.getenv('TRYONAI_ACCESS_TOKEN')}",
        }

        response = requests.post(url, headers=headers, data=kwargs)
        if response.status_code != 200:
            raise Exception(f"Failed to create experiment: {response.text}")
        else:
            return response.json()
        
    except Exception as e:
        raise Exception(f"Failed to create experiment: {e}")

def get_experiment(experiment_id: str):
    """
    Get an experiment.

    Args:
        experiment_id (str): The ID of the experiment.

    Returns:
        dict: The response from the server.
    """
    try:
        url = os.getenv("TRYONAI_SERVER_URL") + f"/api/v1/experiment/{experiment_id}/"
        headers = {
            "Authorization": f"Bearer {os.getenv('TRYONAI_ACCESS_TOKEN')}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to get experiment: {response.text}")
        else:
            return response.json()
    except Exception as e:
        raise Exception(f"Failed to get experiment: {e}")

def download_image(image_url: str, image_path: str):
    """
    Download an image.

    Args:
        image_url (str): The URL of the image to be downloaded.
        image_path (str): The path to the image to be downloaded.

    Returns:
        str: The path to the downloaded image.
    """
    try:
        response = requests.get(image_url)
        if response.status_code != 200:
            raise Exception(f"Failed to download image: {response.text}")
        else:
            with open(image_path, "wb") as f:
                f.write(response.content)
            return image_path
    except Exception as e:
        raise Exception(f"Failed to download image: {e}")
    
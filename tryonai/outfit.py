from .utils import create_experiment

def generate_outfit(params: dict):
    """
    Generate an outfit.

    Args:
        params (dict): The parameters for the outfit generation.

    Returns:
        dict: The response from the server.
    """
    try:
        response = create_experiment(params=str(params), action="generate_outfit")
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to generate outfit: {response.text}")
    except Exception as e:
        raise Exception(f"Failed to generate outfit: {e}")

def caption_outfit(garment_id: str, params: dict):
    """
    Caption an outfit.

    Args:
        garment_id (str): The ID of the garment.
        params (dict): The parameters for the outfit captioning.

    Returns:
        dict: The response from the server.
    """
    try:
        response = create_experiment(garment_id=garment_id, params=str(params), 
                                     action="caption_outfit")
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to caption outfit: {response.text}")
    except Exception as e:
        raise Exception(f"Failed to caption outfit: {e}")

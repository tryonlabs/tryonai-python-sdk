from .utils import create_experiment

def perform_model_swap(garment_id: str, params: dict):
    """
    Perform a model swap.

    Args:
        garment_id (str): The ID of the garment.
        params (dict): The parameters for the model swap.

    Returns:
        dict: The response from the server.
    """
    try:
        response = create_experiment(garment_id=garment_id, params=str(params), 
                                     action="model_swap")
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to perform model swap: {response.text}")
    except Exception as e:
        raise Exception(f"Failed to perform model swap: {e}")

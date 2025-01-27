from .utils import upload_image, create_experiment

def perform_virtual_try_on(garment_id: str, person_id: str):
    """
    Perform a virtual try on.

    Args:
        garment_id (str): The ID of the garment.
        person_id (str): The ID of the person.

    Returns:
        dict: The response from the server.
    """
    try:
        response = create_experiment(garment_id=garment_id, person_id=person_id, action="virtual_try_on")
        return response
    except Exception as e:
        raise Exception(f"Failed to perform virtual try on: {e}")

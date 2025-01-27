# TryOn AI Python SDK
Use this SDK to interact with TryOn AI API. Integrate virtual try-on, model swap, outfit generation and captioning in your application.

## Installation
```bash
pip install tryonai
```

## Environment Variables
```bash
export TRYONAI_SERVER_URL=https://prod.server.tryonlabs.ai
export TRYONAI_EMAIL=your_email@example.com
export TRYONAI_PASSWORD=your_password
export TRYONAI_ACCESS_TOKEN=your_access_token
```

# Usage
## Get access token
```python
from tryonai import get_access_token

# Get access token
access_token = get_access_token(email=os.getenv('TRYONAI_EMAIL'), password=os.getenv('TRYONAI_PASSWORD'))
print("access_token:", access_token)
```
Note: Put the access token in the environment variable `TRYONAI_ACCESS_TOKEN`.

## Upload Image
```python
from tryonai import upload_image

# Upload image
uploaded_image = upload_image(image_path="data/garment.jpg", data={"type": "garment", "gender": "male", "preprocess": "true"}, access_token=access_token)
print("uploaded_image:", uploaded_image)
```

## Virtual Try On
```python
from tryonai import perform_virtual_try_on

# Perform virtual try on
experiment = perform_virtual_try_on(garment_id=garment_id, person_id=person_id)
print("experiment:", experiment)
```

## Model Swap
```python
from tryonai import perform_model_swap

# Perform model swap
experiment = perform_model_swap(garment_id=garment_id, params={"prompt": "Indian male model with straight hair, blue eyes, round face, 4k resolution, high-resolution", "guidance_scale": 4.5, "num_inference_steps": 30, "seed":-1, "num_images": 3, "width":512, "height": 512})
print("experiment:", experiment)
```

## Outfit Generation
```python
from tryonai import generate_outfit

# Generate outfit
experiment = generate_outfit(params={"prompt": "A flat lay image of a T-shirt, round neck, blue color, high-resolution, 4k resolution", "height":256, "width": 256, "seed": -1, "guidance_scale": 4.5, "num_inference_steps": 20, "num_images_per_prompt": 2, "strength": 0.8})
print("experiment:", experiment)
```

## Outfit Captioning
```python
from tryonai import caption_outfit

# Caption outfit
experiment = caption_outfit(garment_id=garment_id, params={"output_format": "text"})
print("experiment:", experiment)
```

## Get Experiment
```python
from tryonai import get_experiment

# Get experiment
experiment = get_experiment(experiment_id=experiment_id)
print("experiment:", experiment)
```

## Download Image
```python
from tryonai import download_image

# Download image
download_image(image_url=experiment_result_image_url, image_path="data/result.png")
```
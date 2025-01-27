from dotenv import load_dotenv

load_dotenv()

import os
import argparse

from tryonai import get_access_token, upload_image, perform_virtual_try_on, get_experiment, download_image, perform_model_swap, generate_outfit, caption_outfit

if __name__ == "__main__":  
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--action", type=str, required=True)
    
    # virtual try-on
    argparser.add_argument("--garment_id", type=str, required=False, default="")
    argparser.add_argument("--person_id", type=str, required=False, default="")
    
    # model swap, outfit generation & captioning
    argparser.add_argument("--prompt", type=str, required=False, default="")
    argparser.add_argument("--guidance_scale", type=float, required=False, default=4.5)
    argparser.add_argument("--num_inference_steps", type=int, required=False, default=30)
    argparser.add_argument("--seed", type=int, required=False, default=-1)
    argparser.add_argument("--num_images", type=int, required=False, default=3)
    argparser.add_argument("--width", type=int, required=False, default=512)
    argparser.add_argument("--height", type=int, required=False, default=512)
    argparser.add_argument("--output_format", type=str, required=False, default="json")
    argparser.add_argument("--strength", type=float, required=False, default=0.8)
    
    # authentication
    argparser.add_argument("--email", type=str, required=False, default="")
    argparser.add_argument("--password", type=str, required=False, default="")
    
    # image upload
    argparser.add_argument("--image_path", type=str, required=False, default="")
    argparser.add_argument("--type", type=str, required=False, default="garment")
    argparser.add_argument("--gender", type=str, required=False, default="male")
    argparser.add_argument("--preprocess", type=str, required=False, default="false")
    
    # download
    argparser.add_argument("--image_url", type=str, required=False, default="")
    argparser.add_argument("--output_path", type=str, required=False, default="")
    
    args = argparser.parse_args()
    
    if args.action == "get_access_token":
        if args.email == "" or args.password == "":
            raise Exception("Email and password are required for getting access token")
        access_token = get_access_token(args.email, args.password)
        print("access token:", access_token)
    elif args.action == "upload_image":
        if args.image_path == "":
            raise Exception("Image path is required for uploading image")
        params = {"type": args.type, "gender": args.gender, "preprocess": args.preprocess}
        uploaded_image = upload_image(args.image_path, data=params)
        print("uploaded image with id:", uploaded_image["id"])
    elif args.action == "virtual_try_on":
        if args.garment_id == "" or args.person_id == "":
            raise Exception("Garment ID and person ID are required for virtual try-on")
        experiment = perform_virtual_try_on(args.garment_id, args.person_id)
        print("experiment:", experiment)
    elif args.action == "model_swap":
        if args.prompt == "" or args.garment_id == "":
            raise Exception("Prompt and garment ID are required for model swap")
        params = {"prompt": args.prompt, "guidance_scale": args.guidance_scale, "num_inference_steps": args.num_inference_steps, "seed": args.seed, 
                  "num_images": args.num_images, "width": args.width, "height": args.height}
        experiment = perform_model_swap(args.garment_id, params)
        print("experiment:", experiment)
    elif args.action == "generate_outfit":
        if args.prompt == "":
            raise Exception("Prompt is required for outfit generation")
        params = {"prompt": args.prompt, "height":args.height, "width": args.width, "seed": args.seed, "guidance_scale": args.guidance_scale, 
                  "num_inference_steps": args.num_inference_steps, "num_images_per_prompt": args.num_images, "strength": args.strength}
        experiment = generate_outfit(params)
        print("experiment:", experiment)
    elif args.action == "caption_outfit":
        if args.garment_id == "":
            raise Exception("Garment ID is required for outfit captioning")
        params = {"output_format": args.output_format}
        experiment = caption_outfit(args.garment_id, params)
        print("experiment:", experiment)
    elif args.action == "get_experiment":
        if args.experiment_id == "":
            raise Exception("Experiment ID is required for getting experiment")
        experiment = get_experiment(args.experiment_id)
        print("experiment:", experiment)
    elif args.action == "download_image":
        if args.image_url == "" or args.output_path == "":
            raise Exception("Image URL and output path are required for downloading image")
        image_url = os.path.join(os.getenv('TRYONAI_SERVER_URL'), args.image_url)
        download_image(image_url, args.output_path)
        print("image downloaded to:", args.output_path)
    else:
        raise Exception("Invalid action")

import datetime
import os

import openai
import requests
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# set a directory to save DALL·E images to
image_dir_name = "static/images"
image_dir = os.path.join(os.curdir, image_dir_name)

def generate_image(suffix: str, prompt: str):
    # call the OpenAI API
    generation_response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url",
    )

    # print response
    print(generation_response)

    # save the image
    prefix = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    generated_image_name = f"{prefix}-{suffix}.png"  # the filetype should be .png
    generated_image_filepath = os.path.join(image_dir, generated_image_name)
    generated_image_url = generation_response["data"][0]["url"]  # extract image URL
    generated_image = requests.get(generated_image_url).content  # download the image

    with open(generated_image_filepath, "wb") as image_file:
        image_file.write(generated_image)  # write the image to the file

    # convert to a web image
    web_image_filepath = os.path.join(image_dir, f"{suffix}.jpg")
    resize_and_optimize_image(generated_image_filepath, web_image_filepath, 1024)

def resize_and_optimize_image(input_path, output_path, width):
    # Open the image using PIL
    image = Image.open(input_path)

    # Resize the image while maintaining the aspect ratio
    height = int((width / float(image.width)) * image.height)
    resized_image = image.resize((width, height), Image.LANCZOS)

    # Optimize and save the resized image
    resized_image.save(output_path, optimize=True, quality=80)

if __name__ == '__main__':
    import personas
    for persona in personas.personas:
        for index, prompt in enumerate(persona["prompt"]):
            suffix = "{code}-{index}".format_map({
                "code": persona["code"],
                "index": index,
            })
            generate_image(
                prompt=prompt,
                suffix=suffix,
            )
    # parser = argparse.ArgumentParser(description='Generate an image using Dall-E.')
    # parser.add_argument('--prompt', type=str, required=True)
    # parser.add_argument('--suffix', type=str, required=True)
    # args = parser.parse_args()
    # generate_image(
    #     prompt=args.prompt,
    #     suffix=args.suffix,
    # )

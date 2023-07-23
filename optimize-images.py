import os
import re

from PIL import Image


def resize_and_optimize_image(input_path, output_path):
    # Open the image using PIL
    image = Image.open(input_path).convert('RGB')
    # Optimize and save the resized image
    image.save(output_path, optimize=True, quality=60)

# 896 × 512
if __name__ == '__main__':
    directory = "static/images"
    for image in os.listdir(directory):
        if image.endswith(".png"):
            if re.match(r"\d+_", image):
                print(f"background-image: url('/static/images/{image}');")
                resize_and_optimize_image(
                    input_path=os.path.join(directory, image),
                    output_path=os.path.join(directory, image.replace(".png", ".jpg")),
                )

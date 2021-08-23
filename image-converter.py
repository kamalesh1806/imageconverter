import sys
import os
from PIL import Image

images_folder = sys.argv[1]
converted_images_folder = sys.argv[2]
# getting input to which type to be converted
type_to_be_converted = sys.argv[3]
type = type_to_be_converted.lower()
if not (os.path.exists(converted_images_folder)):
    os.mkdir(converted_images_folder)
try:
    for filename in os.listdir(images_folder):
        just_name = os.path.splitext(filename)[0]
        img = Image.open(f"{images_folder}{filename}")
        img.save(f"{converted_images_folder}/{just_name}.{type}", f"{type}")
        print(f"converted into {type}")
except:
    print("Something went wrong...check and try again eg:PNG, JPG, PDF, TIFF, BMP, GIF")

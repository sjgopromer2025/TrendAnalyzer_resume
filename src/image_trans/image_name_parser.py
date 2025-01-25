from utils.directory_util import image_directory
from utils.env_path_util import trans_image_path
import os
image_files = image_directory()

image_name_list = [image.split("\\")[-1].split(".")[0] for image in image_files]
image_name_string = ",".join(image_name_list)    
print(image_name_string)


from PIL import Image
from utils.directory_util import image_directory
from utils.env_path_util import trans_image_path
import os
image_files = image_directory()


for image in image_files:
    
    image_name=image.split("\\")[-1]
    # 이미지 파일 열기
    image_file = Image.open(image)

    # 1000x1000으로 크기 조정
    image_resized = image_file.resize((1000, 1300))
    # 저장하기 (필요에 따라 저장 경로와 파일 이름을 변경할 수 있습니다)
    image_resized.save(os.path.join(trans_image_path,f"resized_{image_name}"))
    

image_name_list = [image.split("\\")[-1].split(".")[0] for image in image_files]
image_name_string = ",".join(image_name_list)    
print(image_name_string)


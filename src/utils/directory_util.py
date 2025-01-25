import json
import os
from utils.env_path_util import image_path
from utils.env_path_util import base_path


# 데이터 폴더 월 전체 검사
def image_directory():
    #display 기준 파일 경로
    image_folder = os.path.join(base_path,image_path)
    
    # 디렉토리 내 모든 파일 목록 가져오기
    image_files = os.listdir(image_folder)
    
    return [ os.path.join(image_folder,image) for image in image_files]

    # for image in image_files:
    #     display_year_path = os.path.join(display_path,id,year)
    #     # print(display_year_path)
    #     # print(month_dirs)
    #     display_csv_path = os.path.join(display_year_path,month)
        
    #     display_info_dict[id]= []
    #     # print(display_csv_path)
    #     if os.path.exists(display_csv_path):
    #         csv_files = os.listdir(display_csv_path)
    #         # print(csv_files)
    #         for file in csv_files:
    #             file_path = os.path.join(display_csv_path,file)
    #             display_info_dict[id].append(file_path) 
    #     else:
    #         continue
      
            

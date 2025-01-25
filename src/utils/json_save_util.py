import json
from .env_path_util import processed_path
from .datetime_util import current_time


# 이미지 파일로 저장
# image_save_path = os.path.join(report_path,display_name,"view_time",year,month)
# os.makedirs(image_save_path, exist_ok=True)

def keyword_trend_result_save(result_data):
    # 에러 파일 json 파일 저장
    json_file_path = f'{processed_path}/keyword_trend_{current_time}.json'
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=4) 
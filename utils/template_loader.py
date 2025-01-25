from fastapi.templating import Jinja2Templates
from pathlib import Path
import os 
# 템플릿 디렉토리 경로 설정
templates = Jinja2Templates(directory="templates")

# 템플릿 디렉토리의 루트 설정
TEMPLATES_ROOT = Path(__file__).parent.parent / "templates"

# 특정 디렉토리 경로를 쉽게 가져올 수 있도록 함수 추가
def get_template_path(subdir: str, template_name: str) -> str:
    """
    하위 디렉토리와 템플릿 이름을 조합하여 전체 경로 반환
    """
    return f"{subdir}/{template_name}.html"  # 슬래시 사용





# def get_template_path(base_path: str, filename: str) -> str:
#     """
#     BaseFilePath와 파일명을 조합해 자동으로 경로를 반환하는 전역 함수
#     :param base_path: 템플릿의 기본 경로
#     :param filename: 파일명 (확장자 제외)
#     """
#     return f"{base_path}/{filename}.html"

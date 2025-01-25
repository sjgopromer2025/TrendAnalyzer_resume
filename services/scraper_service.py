from PIL import Image
from typing import List, Optional
import os
from src.utils.env_path_util import image_path

from analysis.data_lab_keyword_collector import CategoryScraper


class scraperService:
    def __init__(self):
        self.upload_dir = image_path
        # 업로드 디렉토리가 없으면 생성
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

    async def get_coupang_category(self, item_name):
        categoryScraper = CategoryScraper()
        result = await categoryScraper.get_coupang_category(item_name)

        return result

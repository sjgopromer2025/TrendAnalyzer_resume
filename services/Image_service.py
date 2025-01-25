from PIL import Image
from typing import List, Optional
import os
from src.utils.env_path_util import image_path

class ImageService:
    def __init__(self):
        self.upload_dir = image_path

        # 업로드 디렉토리가 없으면 생성
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

    async def save_and_resize_images(self, files: List, width: Optional[int], height: Optional[int]) -> List[dict]:
        """
        이미지 파일을 저장하고, 필요하면 크기 조정.

        Args:
            files: 업로드된 이미지 파일 리스트.
            widths: 각 이미지의 너비 리스트.
            heights: 각 이미지의 높이 리스트.

        Returns:
            처리된 이미지에 대한 결과 리스트.
        """
        response = []

        for idx, file in enumerate(files):
            try:
                # 업로드된 파일 저장
                file_path = os.path.join(self.upload_dir, file.filename)
                with open(file_path, "wb") as f:
                    content = await file.read()
                    f.write(content)
            
                if width and height:  # 크기 정보가 존재하는 경우만 처리
                    with Image.open(file_path) as img:
                        resized_img = img.resize((int(width), int(height)))
                        resized_img.save(file_path)  # 원본 파일 덮어쓰기

                response.append({
                    "filename": file.filename,
                    "status": "success",
                    "path": file_path,
                })
            except Exception as e:
                response.append({
                    "filename": file.filename,
                    "status": "error",
                    "error": str(e),
                })

        return response


from fastapi import APIRouter
from routes import image_upload, index
from routes.scraper import scraper

router = APIRouter()

# 각 모듈의 라우터를 등록
router.include_router(image_upload.router, prefix="/image", tags=["Image"])
router.include_router(index.router, prefix="", tags=["index"])
router.include_router(scraper.router, prefix="/scraper", tags=["Scraper"])


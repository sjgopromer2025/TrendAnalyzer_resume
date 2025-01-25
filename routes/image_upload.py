from fastapi import Depends, Path, HTTPException, APIRouter, File,UploadFile,Form
from fastapi import Request
from typing import List,Dict
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from services.Image_service import ImageService
from utils.template_loader import templates

router = APIRouter()

# ImageService 인스턴스 생성
image_service = ImageService()

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("file_upload/upload3.html", {"request": request})

@router.post("/upload/test")
async def image_resize(
    files: List[UploadFile] = File(...), 
    width: int = Form(...),  # 단일 너비
    height: int = Form(...)  # 단일 높이
):
    response = await image_service.save_and_resize_images(files, height, width)
    return {"data": response}



######################################
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.utils.template_loader import templates, get_template_path

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_upload_page(request: Request):
    # 템플릿 경로를 지정하지 않으면 기본 templates 디렉토리를 기준으로 찾음
    return templates.TemplateResponse("uploads/upload.html", {"request": request})

@router.get("/preview", response_class=HTMLResponse)
async def read_preview_page(request: Request):
    # 유틸리티 함수로 경로 생성
    template_path = get_template_path("uploads", "preview.html")
    return templates.TemplateResponse(template_path, {"request": request})

"""
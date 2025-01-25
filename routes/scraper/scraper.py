from fastapi import Depends, Path, HTTPException, APIRouter, File, UploadFile, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from services.scraper_service import scraperService
from utils.template_loader import templates, get_template_path

router = APIRouter()

# ImageService 인스턴스 생성
scraper_service = scraperService()

base_path = "scraper"


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    template_path = get_template_path(base_path, "category_scraper")

    return templates.TemplateResponse(template_path, {"request": request})


@router.post("/category")
async def get_category(request: Request):
    data = await request.json()
    item_name = data.get("item_name", "")
    category = data.get("category", "")
    response = await scraper_service.get_coupang_category(item_name)

    return response

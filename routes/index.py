from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from utils.template_loader import templates

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

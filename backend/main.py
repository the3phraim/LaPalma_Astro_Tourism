from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Get the absolute path of the frontend folder
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = BASE_DIR / "index.html"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = TEMPLATE_PATH.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

# Define static files directory
STATIC_PATH = BASE_DIR / "static"

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

# starte server: cd backend -> uvicorn main:app --reload 
# port: http://127.0.0.1:8000
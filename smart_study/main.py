from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from routers import levels, classes, subjects, notes

app = FastAPI(title="Smart Study Pro-Notes API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(levels.router, prefix="/api")
app.include_router(classes.router, prefix="/api")
app.include_router(subjects.router, prefix="/api")
app.include_router(notes.router, prefix="/api")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

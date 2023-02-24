import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home.html", context)
    

@app.get("/api/v1/hello-world/")
def read_hello_world():
    """
    Return an API-like response.
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}



# first created view function
# left in for reference
# removed in chapter 3 branch and final code
# @app.get("/")
# def read_index():
#     """
#     Return a Python Dictionary that supports JSON serialization.
#     """
#     return {"Hello": "World"} 
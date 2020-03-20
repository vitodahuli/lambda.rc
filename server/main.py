from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('home.html', {
        'request': request,
        'ctx': {'title': 'lambda RC - IT riders club.'}})

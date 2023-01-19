from typing import Optional, List
from fastapi import FastAPI, Request, HTTPException, Depends, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Field, Session, SQLModel, create_engine, select
import uvicorn


app = FastAPI()

app.mount('/assets', StaticFiles(directory='assets'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request, title: Optional[str] = None):
    title = 'Wacca Engineer'
    context = {
        'request': request,
        'title': title,
    }
    return templates.TemplateResponse('index.html', context)


@app.get('/items/{id}', response_class=HTMLResponse)
async def items(request: Request, id: str):
    context ={
        'request': request,
        'id': id,
    }
    return templates.TemplateResponse('items.html', context)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

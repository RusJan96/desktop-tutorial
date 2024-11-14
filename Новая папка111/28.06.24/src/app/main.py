from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from typing import Annotated
from fastapi.responses import FileResponse
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")


#Ендпоинт который возвращает HTML страницу пользователя
@app.get('/') #http://127.0.0.1.8000/
def index_page(request:Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get('/api/images/all')
def get_images(request: Request):
    pass
    return FileResponse(path="")

@app.post("/api/images/upload")
def upload_images(request:Request, file: Annotated[bytes, File()]):
    name_file = f"img_{len(os.listdir('images/'))}"    
    with open(f'images/{name_file}', 'wb') as file_save:
        file_save.write(file)
    return {"message": "Успешно загружен на сервер"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
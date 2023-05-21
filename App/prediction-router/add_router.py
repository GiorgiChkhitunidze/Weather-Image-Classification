from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from typing import List
import numpy as np

import prediction_router.prediction_functions as pred_func
import prediction_router.load_models as loader
import prediction_router.embaddings as embs


router = APIRouter()

templates = Jinja2Templates(directory="templates")


model = loader.get_model()
weather_embs = embs.weather_embs

@router.post("/prediction/", response_class=HTMLResponse)
async def create_upload_files(request: Request, files: List[UploadFile] = File(...)):
    file = files[0]
    image_path = '/static/image_base/'+str(file.filename) # for displaying images

    image = pred_func.read_image(await file.read())
    image.save('static/image_base/' + file.filename)
    image = pred_func.preprocess(image)

    prediction = pred_func.predict(image, model, weather_embs)

    content1 = f"Weather: {prediction}"
    return templates.TemplateResponse("post_index.html", {"request": request, "content1": content1, "image_path": image_path})
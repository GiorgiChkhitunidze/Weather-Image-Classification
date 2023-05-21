from PIL import Image
from io import BytesIO
import torch
import numpy as np



def read_image(file: Image.Image):
    image = Image.open(BytesIO(file))
    return image


def preprocess(image: Image.Image):
    image = image.convert('RGB').resize((224,224), Image.NEAREST)
    image = torch.tensor(np.array(image).reshape((3, 224, 224)), dtype=torch.float32)
    return image


def predict(image, model, embadings):
    model.eval()
    with torch.no_grad():
        output = model(image.unsqueeze(0))
        predictions = int(output.argmax(axis=1))
        predictions = embadings[predictions]
    return predictions
# Weather classification
This repo is divided in two parts:
1. Train Weather Models
2. Built Weather Image Classifier App Using FastAPI

### Train Weather Models
I built custom model from scratch and compared it to several popular pretrained models such as: *Resnet18*, *Resnet50*, *Resnet152*, *Alexnet* and *Densenet*. Only showing those that produced most promising results. Eventually *Densenet* turned out to be the best.
You can check *weather-prediction.ipynb* on this <a href="https://nbviewer.org/github/GiorgiChkhitunidze/Weather-Recognition/blob/main/weather-prediction.ipynb#imports">nbviewer link</a> without any rendering problem.

### Built Weather Image Classifier App Using FastAPI
In the folder ***App*** I built simple Weather Prediction App using FastAPI which can be run on uvicorn server.
Here you can see how the app works:

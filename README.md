# Weather classification
This repo is divided in two parts:
1. Train Weather Classifier Models
2. Built Weather Image Classifier App Using FastAPI

### Train Weather Models
I built custom model from scratch and compared it to several popular pretrained models such as: *Resnet18*, *Resnet50*, *Resnet152*, *Alexnet* and *Densenet*. Only showing those that produced most promising results. Eventually *Densenet* turned out to be the best.
You can check *weather-prediction.ipynb* on this <a href="https://nbviewer.org/github/GiorgiChkhitunidze/Weather-Image-Classification/blob/main/weather-prediction.ipynb">nbviewer link</a> without any rendering problem.
These are the whether Categories:
- dew
- fogsmog
- frost
- glaze
- hail
- lightning
- rain
- rainbow
- rime
- sandstorm
- snow

### Built Weather Image Classifier App Using FastAPI
In the folder ***App*** I built simple Weather Prediction App. I wrapped the best model into FastAPI and Styled using HTML/CSS/JavaScript. It can be run on uvicorn server.
Here you can see how the app works:


https://github.com/GiorgiChkhitunidze/Weather-Image-Classification/assets/112623714/da54d557-70c5-42e9-9d13-f051b79e6302


## References and Acknowledgements:
- Model is trained on a <a href="https://www.kaggle.com/datasets/jehanbhathena/weather-dataset">Weather Image Recognition Dataset</a> on Kaggle.
- App background image by <a href="https://pixabay.com/users/pexels-2286921/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1245817">Pexels</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1245817">Pixabay</a>
- Social media preview image by <a href="https://pixabay.com/users/cromaconceptovisual-4595909/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5940755">cromaconceptovisual</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5940755">Pixabay</a>

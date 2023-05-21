import torch
from torch import nn
from torchvision import models

device = torch.device('cpu')

def get_model():
    model = models.densenet121(weights='DenseNet121_Weights.DEFAULT')
    for param in model.parameters():
        param.requires_grad = False
    num_ftrs = model.classifier.in_features
    model.classifier = nn.Linear(num_ftrs, 11)
    model.load_state_dict(torch.load("../app/model/densenet_fine_tuned.pt", device))
    return model



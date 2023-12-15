import torch
import torch.nn as nn
import torchvision

class WhiteNet(torch.nn.Module):
    def __init__(self):
        super(WhiteNet, self).__init__()

        self.input = torch.nn.Sequential(
                torch.nn.Linear(225, 225), 
                torch.nn.ReLU(),
                torch.nn.Linear(225, 256),
                torch.nn.ReLU(),
                torch.nn.Linear(256, 256),
                torch.nn.ReLU(),
                torch.nn.Linear(256, 289),
                torch.nn.ReLU(),
                torch.nn.Linear(289, 289),
                torch.nn.ReLU(),
                torch.nn.Linear(289, 324),
                torch.nn.ReLU(),
                torch.nn.Linear(324, 324),
                torch.nn.ReLU(),
                torch.nn.Linear(324, 324),
                torch.nn.ReLU(),
                torch.nn.Linear(324, 225) )
        
    def forward(self, x):
        x = self.input(x)
        return x